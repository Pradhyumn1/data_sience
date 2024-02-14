from src.my_mlproject.logger import logging
from src.my_mlproject.exception import CustomException
from src.my_mlproject.components.data_ingestion import DataIngestion
from src.my_mlproject.components.data_ingestion import DataIngestionConfig
from src.my_mlproject.components.data_transformation import DataTransformationConfig,DataTransformation
from src.my_mlproject.components.model_tranier import ModelTrainerConfig,ModelTrainer

import sys
import mlflow


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # Add debugging statements here
        mlflow_tracking_uri = "https://dagshub.com/Pradhyumn1/sudent_data_insights.mlflo"
        mlflow_tracking_username = "Pradhyumn1"
        mlflow_tracking_password = "9668024cdf3cab6718afb606d69ebde8f71b7dcf"

        print("MLflow Tracking URI:", mlflow_tracking_uri)
        print("MLflow Tracking Username:", mlflow_tracking_username)
        print("MLflow Tracking Password:", mlflow_tracking_password)

        mlflow.set_registry_uri(mlflow_tracking_uri)
        mlflow.set_tracking_uri(mlflow_tracking_uri)

        
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

        ## Model Training

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)