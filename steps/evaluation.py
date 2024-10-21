import logging
import pandas as pd
from zenml import step

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@step
def evaluate_model(model, df: pd.DataFrame) -> None:
    logging.info("Evaluating model")
    # Perform evaluation operations...
    # For example:
    # score = model.evaluate(df)
    # logging.info(f"Model score: {score}")
    pass