import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Cleaning data")
    # Perform cleaning operations...
    # For example:
    # df = df.dropna()
    return df