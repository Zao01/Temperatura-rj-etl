
from src.pipeline import setup_logging, extract_data, transform_data, load_data, send_email

def pipeline_etl(request):
    setup_logging()
    try:
        url = "https://archive-api.open-meteo.com/v1/archive"
        params = {
            "latitude": -22.9,
            "longitude": -43.2,
            "start_date": "2023-01-01",
            "end_date": "2023-12-31",
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "America/Sao_Paulo"
        }
        raw_path = "/tmp/temperatura_rj.csv"
        processed_path = "/tmp/temperatura_rj_tratada.csv"
        db_path = "/tmp/temperatura.db"

        extract_data(url, params, raw_path)
        transform_data(raw_path, processed_path)
        load_data(processed_path, db_path)

        send_email("Pipeline executado com sucesso", "O pipeline ETL foi executado com sucesso.")
        return "Pipeline executado com sucesso"

    except Exception as e:
        send_email("Pipeline falhou", f"Erro: {e}")
        return f"Erro: {e}"


