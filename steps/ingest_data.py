import logging
import pandas as pd
from zenml import step

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@step
def ingest_df(data_path: str) -> pd.DataFrame:
    """ Ingest data from data_path """
    try:
        logging.info(f"Ingesting data from {data_path}")
        df = pd.read_csv(data_path)
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e