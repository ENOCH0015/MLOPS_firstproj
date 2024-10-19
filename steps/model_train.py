import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def train_model(df: pd.DataFrame):
    logging.info("Training model")
    # Perform training operations...
    # For example:
    # model = SomeModel()
    # model.fit(df)
    return "trained_model"  # Replace with actual trained model