import pandas as pd
import requests
import sqlite3
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def setup_logging():
    logging.basicConfig(
        filename='pipeline.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def extract_data(url, params, raw_path):
    logging.info("Iniciando extração.")
    
    response = requests.get(url, params=params) 

    if response.status_code != 200:
        logging.error(f"Erro na extração: {response.status_code}")
        raise Exception(f"Erro na extração: {response.status_code}")

    data = response.json()
    df = pd.DataFrame(data["daily"])
    df["temperature_2m_avg"] = (df["temperature_2m_max"] + df["temperature_2m_min"]) / 2
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    df.to_csv(raw_path, index=False)
    logging.info("Extração concluída.")


def transform_data(raw_path, processed_path):
    logging.info("Iniciando transformação.")
    df = pd.read_csv(raw_path)
    df["time"] = pd.to_datetime(df["time"])
    df["month"] = df["time"].dt.to_period("M").astype(str)
    df["weekday"] = df["time"].dt.day_name()
    df[["temperature_2m_max", "temperature_2m_min", "temperature_2m_avg"]] = df[["temperature_2m_max", "temperature_2m_min", "temperature_2m_avg"]].round(1)
    monthly_avg = df.groupby("month")[["temperature_2m_avg"]].mean().reset_index()
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    monthly_avg.to_csv(processed_path, index=False)
    logging.info("Transformação concluída.")

def load_data(processed_path, db_path):
    logging.info("Iniciando carga.")
    df = pd.read_csv(processed_path)
    conn = sqlite3.connect(db_path)
    df.to_sql("temperatura_mensal", conn, if_exists="replace", index=False)
    conn.close()
    logging.info("Carga concluída.")



def send_email(subject, body):
    sender_email = os.getenv("EMAIL_USER")
    receiver_email = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")


    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")


