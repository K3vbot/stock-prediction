""" Importing Neccesary Packages """

import pandas as pd
from pandas_datareader import DataReader, get_data_yahoo
from datetime import datetime
import numpy as np
import csv
import os


path = r"C:\Users\keval\Coding Projects\Stock_Market_Predictor\Stock Files"

""" Creating Indivual Stock Files Using Pandas DataReader """
def create_stockdir():
    with open("Stocks.csv") as file:
        reader = csv.reader(file)
        header = next(reader)
        if header != None:
            for row in reader:
                stock = row[1]
                df = DataReader(stock, data_source="yahoo", start="2011-01-01", end=datetime.now())
                df.drop(["Adj Close"], axis=1)
                df.to_csv(path + f"\{stock}.csv")

create_stockdir()

""" Iterating Over Every Single Stock File in the Folder """
def get_stock_csv(listdir, stock_ticker):
    stock_files = os.listdir(listdir)

    for stock_file in stock_files:
        if stock_file.endswith(".csv"):
            if stock_file == (stock_ticker + ".csv"):
                df = pd.read_csv(path + f"\{stock_file}")
    
    return df

""" Data Preprocessing For 1 Day to 1 Day """


