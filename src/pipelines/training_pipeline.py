import os
import sys
from os.path import dirname, join, abspath

# Add project directory to sys.path for module imports
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from logger import logging
from exception import CustomException
from src.components.data_ingestion import DataIngestion
# from src.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer

if __name__ == '__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)
#     try:
#         # Step 1: Data Ingestion
#         logging.info("Starting Data Ingestion...")
#         data_ingestion = DataIngestion()
#         train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
#         print(f"Train Data Path: {train_data_path}, Test Data Path: {test_data_path}")

#         # Step 2: Data Transformation
#         logging.info("Starting Data Transformation...")
#         data_transformation = DataTransformation()
#         transformed_data_path = data_transformation.initaite_data_transformation(
#             train_data_path, test_data_path
#         )  # If this step produces transformed arrays, handle them accordingly.

#         # Step 3: Model Training
#         logging.info("Starting Model Training...")
#         model_trainer_config = {
#             'trained_model_file_path': 'artifacts/best_model.pkl'  # Path to save the best model
            
#         }
#         logging.info("saved the best model in the artifacts")

#         # train_arr,test_arr,obj_path=data_transformation.initaite_data_transformation(train_data_path,test_data_path)
#         model_trainer = ModelTrainer(model_trainer_config)
#         model_trainer.initiate_model_training(train_data_path,test_data_path)

#         # # Begin model training using transformed data paths
#         # model_trainer.initiate_model_training(
#         #     train_file_path=train_data_path,
#         #     test_file_path=test_data_path
#         # )
#     except Exception as e:
#         logging.error(f"An error occurred in the training pipeline: {e}")
#         raise CustomException(e, sys)
