import requests
import pandas as pd
import os

# Parâmetros da API
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": -22.9,
    "longitude": -43.2,
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "daily": "temperature_2m_max,temperature_2m_min",
    "timezone": "America/Sao_Paulo"
}

# Requisição
response = requests.get(url, params=params)
data = response.json()

# Transformar em DataFrame
df = pd.DataFrame(data["daily"])
df["temperature_2m_avg"] = (df["temperature_2m_max"] + df["temperature_2m_min"]) / 2

# Criar diretório
os.makedirs("C:/Users/User/Desktop/JORNADA ENGENHEIRO DE DADOS/Temperatura-rj-etl/data/raw", exist_ok=True)
df.to_csv("C:/Users/User/Desktop/JORNADA ENGENHEIRO DE DADOS/Temperatura-rj-etl/data/raw/temperatura_rj_2023.csv", index=False)

print("Extração concluída com sucesso.")
