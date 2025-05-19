import pandas as pd
import sqlite3
import os

# Caminho do arquivo tratado
csv_path = "data/processed/temperatura_rj_tratada.csv"
db_path = "data/temperatura.db"

# Lê os dados tratados
df = pd.read_csv(csv_path)

# Cria conexão com o banco SQLite
conn = sqlite3.connect(db_path)

# Salva no banco
df.to_sql("temperatura_mensal", conn, if_exists="replace", index=False)

# Fecha conexão
conn.close()

print("Carga finalizada com sucesso!")

conn = sqlite3.connect("data/temperatura.db")
df = pd.read_sql("SELECT * FROM temperatura_mensal", conn)
print(df.head())
conn.close()

