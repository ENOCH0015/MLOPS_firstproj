import sys
import os

# Ensure this points to the correct parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from zenml.client import Client
from pipelines.training_pipeline import train_pipeline

# Set the path for artifact store
base_artifact_store_path = r"C:\Users\DELL\Documents\AI engr\Ecommerce mlops\zenml_artifacts"
os.environ["ZENML_ARTIFACT_STORE"] = base_artifact_store_path  # Set environment variable

if __name__ == "__main__":
    # Run pipeline
    train_pipeline(data_path=r"C:\Users\DELL\Documents\AI engr\Ecommerce mlops\DATA\olist_customers_dataset.csv")
