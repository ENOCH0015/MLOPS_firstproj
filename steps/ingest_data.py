import logging
import pandas as pd

from zenml import step

class IngestData: 
    """ 
    Ingest data from the data_path
    """
    def __init__ (self, data_path:str):
        """Initialize the class

        Args:
            data_path (str): path to the data file
        """
        self.data = data_path
        
    def get_data(self):
        logging.info(f"Ingest data from {self.data}")
        return pd.read_csv(self.data)
@step
def ingest_data(data_path:str) -> pd.DataFrame:
    """
    Ingest data from data_path
    
    Args: 
        data_path: path to data
    Returns:
        pd.DataFrame: the ingested data
    """    
    try:
     ingest_data = IngestData(data_path)
     df = ingest_data.get_data()
     return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e
    