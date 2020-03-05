#!/usr/bin/env/python3

import numpy as np
import pandas as pd


class logFile:
    
    def __init__(self,file):
        self.df = pd.read_csv(file, usecols = ['ip','date','time','accession'])
        self.original_df = self.df
        
    def extract(self):
        return self.df
    
    def transformer(self,df):
        self.df = df
        '''
        cleans the data for further manipulation
        input: df
        output: transformed df
        '''
        #setting the datetime
        self.df['datetime'] = self.df['date'] + ' ' + self.df['time']
        self.df['datetime'] = pd.to_datetime(self.df['datetime'])
        
        #Resetting to DatetimeIndex
        self.df = df.set_index(df.datetime)
       
        return self.df

