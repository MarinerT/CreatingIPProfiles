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
        #self.df = df.drop('datetime',axis=1)
        
        #Feature Engineering for Filtering
        
        ## Creating cumulative count columns
        #self.df['ip_ccount'] = (self.df.ip.sort_values(self.df.datetime)).groupby(self.df.accession).cumcount()+1
        #self.df['doc_ccount'] = self.df.groupby(self.df.accession).cumcount()+1
        
        ## Creating total count columns
        #self.df['ip_total_count'] = self.df.groupby(self.df.ip, sort=False)['ip_ccount'].transform(max)
        #self.df['doc_total_count'] = self.df.groupby(self.df.accession, sort=False)['doc_ccount'].transform(max)
        
        return self.df
    
#     def filters(self):
#         #return df.query('200 > ip_total_count > 5 and 200 > doc_total_count > 30 ', inplace=True)
    
#     def stats(self):
# #         self.unique_events = self.df.shape[0]
        
#         #Results of filtering
#         #sample size
#         #loss % of unique docs
#         #loss % of unique ips
    
#     def plot_stats(self):
# #         plt.hist(df1.ip_total_count)
# #         plt.hist(df1.doc_total_count)
    
#     def graph(self, data):
#         pass
    
#     def metrics(self, data):
#         pass
