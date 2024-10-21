import logging
import pandas as pd
from zenml import step

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@step
def train_model(df: pd.DataFrame) -> None:
    logging.info("Training model")
    # Perform training operations...
    # For example:
    # model = SomeModel()
    # model.fit(df)
    pass