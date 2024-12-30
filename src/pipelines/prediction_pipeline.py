import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            data_scaled=preprocessor.transform(features)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
        #Airline	Source	Destination	Total_Stops	Price	Date	Month
        



class CustomData:
    def __init__(self,
                 Airline:str,
                 Source:str,
                 Destination:str,
                 Total_Stops:str,
                 Date:int,
                 Month:int):
                 
        
     
     self.Airline=Airline
     self.Source=Source
     self.Destination=Destination
     self.Total_Stops=Total_Stops
     self.Date=Date
     self.Month=Month
    
    
        

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                
                'Airline':[self.Airline],
                'Source':[self.Source],
                'Destination':[self.Destination],
                'Total_Stops':[self.Total_Stops],
                'Date':[self.Date],
                'Month':[self.Month]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)
   


