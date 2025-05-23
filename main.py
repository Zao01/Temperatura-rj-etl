from src.pipeline import setup_logging, extract_data, transform_data, load_data, send_email
from dotenv import load_dotenv
load_dotenv()


def main():
    setup_logging()
    try:
        # Executa ETL
        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
            "latitude": -22.9,
            "longitude": -43.2,
            "start_date": "2023-01-01",
            "end_date": "2023-12-31",
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "America/Sao_Paulo"
        }
        raw_path = "data/raw/temperatura_rj.csv"
        processed_path = "data/processed/temperatura_rj_tratada.csv"
        db_path = "data/temperatura.db"

        extract_data(url, params, raw_path)
        transform_data(raw_path, processed_path)
        load_data(processed_path, db_path)

        send_email("Pipeline executado com sucesso", "O pipeline ETL foi executado com sucesso.")
    except Exception as e:
        send_email("Pipeline falhou", f"Erro: {e}")
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()

