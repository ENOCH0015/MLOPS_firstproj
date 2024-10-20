import sys
import os
from zenml.client import Client

# Ensure this points to the correct parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluate_model

def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    cleaned_df = clean_df(df)
    trained_model = train_model(cleaned_df)
    evaluate_model(trained_model, cleaned_df)

if __name__ == "__main__":
    # Initialize ZenML client
    client = Client()

    # Set the default stack (replace "your_stack_name" with your actual stack name)
    client.active_stack_model.set_stack("your_stack_name")

    # Define the data path
    data_path = r"C:\Users\DELL\Documents\AI engr\Ecommerce mlops\DATA\olist_customers_dataset.csv"

    # Run pipeline
    train_pipeline(data_path)