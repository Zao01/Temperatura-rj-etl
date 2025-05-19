import pandas as pd
import os

# Carrega dados extraídos
df = pd.read_csv("data/raw/temperatura_rj_2023.csv")

# Converte coluna de data
df["time"] = pd.to_datetime(df["time"])

# Cria colunas auxiliares
df["month"] = df["time"].dt.to_period("M").astype(str)
df["weekday"] = df["time"].dt.day_name()

# Arredonda temperaturas
df["temperature_2m_max"] = df["temperature_2m_max"].round(1)
df["temperature_2m_min"] = df["temperature_2m_min"].round(1)
df["temperature_2m_avg"] = df["temperature_2m_avg"].round(1)

# Agrupa por mês
monthly_avg = df.groupby("month")[["temperature_2m_avg"]].mean().reset_index()
monthly_avg["temperature_2m_avg"] = monthly_avg["temperature_2m_avg"].round(1)

# Cria diretório e salva
os.makedirs("C:/Users/User/Desktop/JORNADA ENGENHEIRO DE DADOS/Temperatura-rj-etl/data/processed", exist_ok=True)
monthly_avg.to_csv("C:/Users/User/Desktop/JORNADA ENGENHEIRO DE DADOS/Temperatura-rj-etl/data/processed/temperatura_rj_tratada.csv", index=False)

print("Transformação finalizada com sucesso.")
