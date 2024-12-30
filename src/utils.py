import os
import sys
import pickle
import numpy as np 
import pandas as pd

from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)


    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

            

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)


def load_object(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('exception occured in load_object function utils')
        raise CustomException(e,sys)
    



    #  <div class="form-row">
    #         <div class="form-group col-md-6">
    #             <label for="Airline">Airline:</label>
    #             <input type="text" class="form-control" id="Airline" name="Airline" placeholder="Select Airline (str)">
    #         </div>
    #         <div class="form-group col-md-6">
    #             <label for="Source">Source:</label>
    #             <input type="text" class="form-control" id="Source" name="Source" placeholder="Select Source (str)">
    #         </div>
    #     </div>

    #     <div class="form-row">
    #         <div class="form-group col-md-6">
    #             <label for="Destination">Destination:</label>
    #             <input type="text" class="form-control" id="Destination" name="Destination" placeholder="Select Destiantion (str))">
    #         </div>
    #         <div class="form-group col-md-6">
    #             <label for="Total_Stops">Total_Stops:</label>
    #             <input type="text" class="form-control" id="Total_Stops" name="Total_Stops" placeholder="Select Total Stops (str)">
    #         </div>

    #         <div class="form-group col-md-6">
    #             <label for="Date">Date:</label>
    #             <input type="text" class="form-control" id="Date" name="Date" placeholder="Select Date of Journey (float)">
    #         </div>
    #         <div class="form-group col-md-6">
    #             <label for="Month">Month:</label>
    #             <input type="text" class="form-control" id="Month" name="Month" placeholder="Select Month of journey (float)">
    #         </div>

    #     </div>

