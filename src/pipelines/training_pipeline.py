import os,sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))

import os
import sys
from logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion

if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path=obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)