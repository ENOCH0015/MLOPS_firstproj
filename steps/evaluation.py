import logging
import pandas as pd
import os
from zenml import step

def setup_logging(step_name):
    log_dir = os.path.join(r"C:\Users\DELL\Documents\AI engr\Ecommerce mlops\zenml_artifacts", step_name, 'logs')
    os.makedirs(log_dir, exist_ok=True)  # Create the log directory if it doesn't exist

    logging.basicConfig(
        filename=os.path.join(log_dir, f'{step_name}.log'),  # Use step-specific log file
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

@step
def evaluate_model(df: pd.DataFrame) -> None:
    setup_logging('evaluate')  # Set up logging for this step
    logging.info("Evaluating model")
    # Perform evaluation operations...
