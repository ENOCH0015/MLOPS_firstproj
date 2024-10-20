import sys
import os
from zenml.client import Client

# Ensure this points to the correct parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipelines.training_pipeline import train_pipeline

if __name__ == "__main__":
    # Initialize ZenML client with explicit artifact store path
    client = Client()
    client.activate_stack(
        stack_name="default",
        artifacts=dict(
            path="C:\\Users\\DELL\\Documents\\AI engr\\Ecommerce mlops\\zenml_artifacts",
            type="local",
        )
    )

    # Define the data path
    data_path = r"C:\Users\DELL\Documents\AI engr\Ecommerce mlops\DATA\olist_customers_dataset.csv"

    # Run pipeline
    train_pipeline(data_path)