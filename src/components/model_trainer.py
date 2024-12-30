# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.neighbors import KNeighborsRegressor
# from src.utils import evaluate_model, save_object
# from src.exception import CustomException
# import logging
# import sys
# import os,sys
# from dataclasses import dataclass

# @dataclass
# class ModelTrainerConfig:
#     model_obj_file_path=os.path.join('artifacts','bestmodel.pkl')

# class ModelTrainer:
#     def __init__(self):
#         self.model_trainer_config=ModelTrainerConfig()


# class ModelTrainer:
#     def initiate_model_training(self,train_array,test_array):
#         try:
#             logging.info('Loading train and test data...')
#             # # Load train and test data
#             # train_df = pd.read_csv(train_file_path)
#             # test_df = pd.read_csv(test_file_path)

#             logging.info('Splitting dependent and independent variables...')
#             # Splitting features (X) and target (y)
#             X_train = train_array.loc[:, :-1].values  # All rows, all columns except the last
#             y_train = train_array.loc[:, -1].values   # All rows, last column
#             X_test = test_array.loc[:, :-1].values
#             y_test = test_array.loc[:, -1].values
#             logging.info('Splitting Dependent and Independent variables from train and test data')
            

#             models = {
                
#                 'KNeighborsRegressor': KNeighborsRegressor(),
#                 'GradientBoostingRegressor': GradientBoostingRegressor(),
#                 'RandomForestRegressor': RandomForestRegressor(),
#                 'DecisionTree': DecisionTreeRegressor()
#             }

#             logging.info('Evaluating models...')
#             # Evaluate models
#             model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)
#             print(model_report)
#             logging.info(f'Model Report: {model_report}')

#             # Identify the best model
#             best_model_score = max(model_report.values())
#             best_model_name = [name for name, score in model_report.items() if score == best_model_score][0]
#             best_model = models[best_model_name]

#             print(f'Best Model Found: {best_model_name} with R2 Score: {best_model_score}')
#             logging.info(f'Best Model Found: {best_model_name} with R2 Score: {best_model_score}')

#             # Save the best model
#             # save_object(
#             #     file_path=self.model_trainer_config.model_obj_file_path,
#             #     obj=best_model
#             # )
            
            
          

#         except Exception as e:
#             logging.error("Exception occurred in the initiate_model_training")
#             raise CustomException(e, sys)




# src/components/model_trainer.py

# import pandas as pd
# import logging
# import sys
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.neighbors import KNeighborsRegressor
# from src.utils import evaluate_model, save_object
# from src.exception import CustomException


# class ModelTrainer:
#     def __init__(self, model_trainer_config):
#         self.model_trainer_config = model_trainer_config

#     def initiate_model_training(self, train_file_path, test_file_path):
#         try:
#             logging.info('Loading train and test data...')
#             # Load train and test data
#             train_df = pd.read_csv(train_file_path)
#             test_df = pd.read_csv(test_file_path)

#             logging.info('Splitting dependent and independent variables...')
#             # Splitting features (X) and target (y)
#             X_train = train_df.iloc[:, :-1].values
#             y_train = train_df.iloc[:, -1].values
#             X_test = test_df.iloc[:, :-1].values
#             y_test = test_df.iloc[:, -1].values

#             models = {
                  
#                 'KNeighborsRegressor': KNeighborsRegressor(),
#                 'GradientBoostingRegressor': GradientBoostingRegressor(),
#                 'RandomForestRegressor': RandomForestRegressor(),
#                 'DecisionTree': DecisionTreeRegressor()
#             }

#             logging.info('Evaluating models...')
#             # Evaluate models
#             model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)
#             print(model_report)
#             logging.info(f'Model Report: {model_report}')

#             # Identify the best model
#             best_model_score = max(model_report.values())
#             best_model_name = [name for name, score in model_report.items() if score == best_model_score][0]
#             best_model = models[best_model_name]

#             print(f'Best Model Found: {best_model_name} with R2 Score: {best_model_score}')
#             logging.info(f'Best Model Found: {best_model_name} with R2 Score: {best_model_score}')

#             # Save the best model
#             save_object(
#                 file_path=self.model_trainer_config['trained_model_file_path'],
#                 obj=best_model
#             )
#             logging.info("best model pkl  file saved")

#         except Exception as e:
#             logging.error("Exception occurred in the initiate_model_training")
#             raise CustomException(e, sys)

