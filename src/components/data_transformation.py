# from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import StandardScaler # HAndling Feature Scaling
# from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding


# from sklearn.pipeline import Pipeline
# from sklearn.compose import ColumnTransformer
# import numpy as np
# import pandas as pd
# from src.exception import CustomException
# from src.logger import logging
# import sys,os
# from dataclasses import dataclass

# @dataclass

# class DataTransformationConfig:
#     preprocessor_obj_file_path=os.path.join('artifacts','preprocesor.pkl') #to save the pkl file path

# class DataTransformation:
#     def __init__(self):
#         self.data_transformation_config=DataTransformationConfig()   

#     def initiate_datatransformation(self, train_df, test_df):
#         try:
#             logging.info("datatransformation started")
            
#             # Separating categorical and numerical features
#             categorical_features = train_df.select_dtypes(include=['object']).columns
#             numerical_features = train_df.select_dtypes(include=['number']).columns




#         except Exception as e:
#             logging.info("Exception occured in the initiate_datatransformation")
#             raise CustomException(e,sys)




# import pandas as pd
# import numpy as np
# import sys,os
# from dataclasses import dataclass

# from sklearn.impute import SimpleImputer ## HAndling Missing Values
# from sklearn.preprocessing import StandardScaler # HAndling Feature Scaling
# from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding
# ## pipelines
# from sklearn.pipeline import Pipeline
# from sklearn.compose import ColumnTransformer

# from src.exception import CustomException
# from src.logger import logging
# from src.utils import save_object


# @dataclass
# class DataTransformationConfig:
#     preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

# class DataTransformation:
#     def __init__(self):
#         self.data_transformation_config=DataTransformationConfig()

#     def get_data_transformation_object(self):
#         try:
#             logging.info('Data Transformation initiated')

#             categorical_cols = ['Airline','Source','Destination','Route'] 
          
#             numerical_cols = ['Price','Total_Stops','journey_day','journey_month', 'dur_min','Dep_Time_hour', 'Dep_Time_minute', 'Arrival_Time_hour','Arrival_Time_minute','dur_hour']
   
#             logging.info('Pipeline Initiated')

#             ## Numerical Pipeline
#             num_pipeline=Pipeline(
#                 steps=[
#                 ('imputer',SimpleImputer(strategy='median')),
#                 ('scaler',StandardScaler())

#                 ]

#             )

#             # Categorigal Pipeline
#             cat_pipeline=Pipeline(
#                 steps=[
#                 ('imputer',SimpleImputer(strategy='most_frequent')),
#                 ('scaler',StandardScaler())
#                 ]

#             )

#             preprocessor=ColumnTransformer([
#             ('num_pipeline',num_pipeline,numerical_cols),
#             ('cat_pipeline',cat_pipeline,categorical_cols)
#             ])
            
#             return preprocessor
#             logging.info('pipeline completed')
            
        
#         except Exception as e:
#             logging.info("Error in Data Trsformation")
#             raise CustomException(e,sys)
        
    
#     def initaite_data_transformation(self, train_data_path, test_data_path):
#         try:
#             # Reading train and test data
#             train_df = pd.read_csv(train_data_path)
#             test_df = pd.read_csv(test_data_path)

#             logging.info('Read train and test data completed')
#             logging.info(f'Train Dataframe Head:\n{train_df.head().to_string()}')
#             logging.info(f'Test Dataframe Head:\n{test_df.head().to_string()}')

#             logging.info('Obtaining preprocessing object')

            

#             preprocessing_obj = self.get_data_transformation_object()

#             # Update column names to match the actual data
#             target_column_name = 'Price'  # Update to actual target column name
#             drop_columns = [target_column_name, 'Total_Stops']  # Update to actual column names

#             # Training data
#             input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
#             target_feature_train_df = train_df[target_column_name]

#             # Test data
#             input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
#             target_feature_test_df = test_df[target_column_name]

#             # Applying transformations
#             input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
#             input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

#             logging.info("Applying preprocessing object on training and testing datasets.")

#             train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
#             test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

#             # Saving the preprocessor object
#             save_object(
#                 file_path=self.data_transformation_config.preprocessor_obj_file_path,
#                 obj=preprocessing_obj
#             )
#             logging.info('Preprocessor pickle file saved')

#             return self.data_transformation_config.preprocessor_obj_file_path #train_arr, test_arr,

#         except Exception as e:
#             logging.error("Exception occurred in the initiate_data_transformation")
#             raise CustomException(e, sys)
        









    # def initaite_data_transformation(self,train_data_path,test_data_path):
    #     try:
    #         # Reading train and test data
    #         train_df = pd.read_csv(train_data_path)
    #         test_df = pd.read_csv(test_data_path)

    #         logging.info('Read train and test data completed')
    #         logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
    #         logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

    #         logging.info('Obtaining preprocessing object')

    #         preprocessing_obj = self.get_data_transformation_object()

    #         target_column_name = 'price'
    #         drop_columns = [target_column_name,'id']
            
    #         #training data
    #         input_feature_train_df = train_df.drop(columns=drop_columns,axis=1)
    #         target_feature_train_df=train_df[target_column_name]

    #         #test data
    #         input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
    #         target_feature_test_df=test_df[target_column_name]
            
    #         ## Transformating using preprocessor obj
    #         input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
    #         input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

    #         logging.info("Applying preprocessing object on training and testing datasets.")
            

    #         train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
    #         test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

    #         save_object(

    #             file_path=self.data_transformation_config.preprocessor_obj_file_path,
    #             obj=preprocessing_obj

    #         )
    #         logging.info('Preprocessor pickle file saved')

    #         return (
    #             train_arr,
    #             test_arr,
    #             self.data_transformation_config.preprocessor_obj_file_path,
    #         )
            
    #     except Exception as e:
    #         logging.info("Exception occured in the initiate_datatransformation")

    #         raise CustomException(e,sys)

