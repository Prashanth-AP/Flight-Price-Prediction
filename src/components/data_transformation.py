from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder


from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


import numpy as np
import pandas as pd
import os,sys
from dataclasses import dataclass



from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass
class DataTransformationConfig():
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl') #to save the pkl file path

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()


    def get_data_transformation_obj(self):
        try:
            logging.info('Data transformation initiated')

            # Divide the columns into categorical and numerical columns
            categorical_cols=['Airline','Source','Destination','Total_Stops']
            numerical_cols=['Date','Month']


            # Define the custom ranking for each ordinal variable
            Airline_categories = ['Air Asia','GoAir','SpiceJet','IndiGo','Trujet','Air India','Vistara','Multiple carriers','Vistara Premium economy','Jet Airways','Multiple carriers Premium economy','Jet Airways Business']
            Source_categories = ['Delhi', 'Mumbai', 'Banglore', 'Kolkata', 'Chennai']
            Destination_categories = ['Delhi','New Delhi','Banglore','Kolkata','Hyderabad','Cochin']
            TotalStops_categories = ['non-stop', '1 stop', '2 stops', '3 stops', '4 stops']

            logging.info('Data transformation pipeline initiated')

            ## Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]

            )

            # Categorigal Pipeline
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[Airline_categories,Source_categories,Destination_categories,TotalStops_categories])),
                ('scaler',StandardScaler())
                ]

            )

            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])


            logging.info('Data transformation pipeline completed')
            return preprocessor
    
        except CustomException as e:
            logging.info("Exception occured in DataTransformation")
            raise CustomException(e,sys)  


    def initaite_data_transformation(self,train_data_path,test_data_path):
        try:
            # Reading train and test data
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_obj()  #to get the preprocessing object file

            target_column_name = 'Price'
            drop_columns = [target_column_name,'Unnamed: 0']     ###@@@

            ## Dividing the dataset into independent and dependent features

            ## For training data
           

            input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column_name]

            ## For test data
            

            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            ## Transformating using preprocessor obj
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training and testing datasets.")
            
           ## combining the Array with the dataframe we use np.c_
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )
            logging.info('Preprocessor pickle file saved')

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )      
        
        except Exception as e:
            logging.info("exception occured in the initiate data transformation")
            raise CustomException(e,sys)