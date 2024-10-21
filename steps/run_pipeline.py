import sys
import os
from zenml.client import Client

# Ensure this points to the correct parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the pipeline
from pipelines.training_pipeline import train_pipeline

if __name__ == "__main__":
    # Initialize ZenML client
    client = Client()

    # Set the active stack (replace "my_new_stack" with your actual stack name)
    client.activate_stack("my_new_stack")

    # Run the pipeline with the dataset path
    train_pipeline(data_path=r"C:\Users\DELL\Documents\AI engr\Ecommerce mlops\DATA\olist_customers_dataset.csv")
