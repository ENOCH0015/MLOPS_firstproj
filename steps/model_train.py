import logging
import pandas as pd
from zenml import step

@step
def train_model(df: pd.DataFrame) -> None:
    """Trians the model on ingested data

    Args:
        df (pd.DataFrame): ingested data
    """
    pass