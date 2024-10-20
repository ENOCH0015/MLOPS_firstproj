import logging
import pandas as pd
from zenml import step

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@step
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Cleaning data")
    # Perform cleaning operations...
    # For example:
    # df = df.dropna()
    return df