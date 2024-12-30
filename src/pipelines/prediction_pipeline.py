# import sys
# import os
# from src.exception import CustomException
# from src.logger import logging
# from src.utils import load_object
# import pandas as pd

# class PredictPipeline:
#     def __init__(self):
#         pass

#     def predict(self,features):
#         try:
#             preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
#             model_path=os.path.join('artifacts','best_model.pkl')

#              # Check if the preprocessor file exists
#             if not os.path.exists(preprocessor_path):
#                 raise FileNotFoundError("Preprocessor file not found in artifacts directory.")

#             # Check if the model file exists
#             if not os.path.exists(model_path):
#                 raise FileNotFoundError("Model file not found in artifacts directory.")

#             preprocessor=load_object(preprocessor_path)
#             model=load_object(model_path)

#             data_scaled=preprocessor.transform(features)

#             pred=model.predict(data_scaled)
#             return pred
            

#         except Exception as e:
#             logging.info("Exception occured in prediction")
#             raise CustomException(e,sys)
        



# class CustomData:
#     def __init__(self,Price:float,
#                  journey_day:int,
#                  journey_month:int,
                
#                  Airline:str,
#                  Source:str,
#                  Destination:str,
#                  Total_Stops:str):
                 
        
#      self.Price=Price
#      self.journey_day=journey_day
#      self.journey_month=journey_month
   
#      self.Airline=Airline
#      self.Source=Source
#      self.Destination=Destination
#      self.Total_Stops=Total_Stops
    
    
        

#     def get_data_as_dataframe(self):
#         try:
#             custom_data_input_dict = {
#                 'Price':[self.Price],
#                 'journey_day':[self.journey_day],
#                 'journey_month':[self.journey_month],
                
#                 'Airline':[self.Airline],
#                 'Source':[self.Source],
#                 'Destination':[self.Destination],
#                 'Total_Stops':[self.Total_Stops]
#             }
#             df = pd.DataFrame(custom_data_input_dict)
#             logging.info('Dataframe Gathered')
#             return df
#         except Exception as e:
#             logging.info('Exception Occured in prediction pipeline')
#             raise CustomException(e,sys)
   


#  Dep_Time_hour:float,
                #  Dep_Time_minute:float,
                #  Arrival_Time_hour:float,
                #  Arrival_Time_minute:float,
                #  dur_hour:float,
                #  dur_min:float,


                 #  self.Dep_Time_hour=Dep_Time_hour
    #  self.Dep_Time_minute=Dep_Time_minute
    #  self.Arrival_Time_hour=Arrival_Time_hour
    #  self.Arrival_Time_minute=Arrival_Time_minute
    #  self.dur_hour=dur_hour
    #  self.dur_min=dur_min


    # 'Dep_Time_hour':[self.Dep_Time_hour],
                # 'Dep_Time_minute':[self.Dep_Time_minute],
                # 'Arrival_Time_hour':[self.Arrival_Time_hour],
                # 'Arrival_Time_minute':[self.Arrival_Time_minute],
                # 'dur_hour':[self.dur_hour],
                # 'dur_min':[self.dur_min],


   
    