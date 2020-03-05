#!/usr/bin/env/python3

from scipy.sparse.linalg import svds
from sklearn.decomposition import NMF
import numpy as np
import pandas as pd

def build_NMF(df,k=50):
'''
Description: builds an NMF model from a Pandas Dataframe
Input: Pandas DataFrame and a value for number of features
Output: ip labels, document labels, and the nmf_matrix
'''
    sparse_matrix = pd.crosstab(df.ip, df.accession)
    model_nmf = NMF(n_components = k
               , init = 'random'
               , random_state = 0)
    m = model_nmf.fit_transform(sparse_matrix)
    h = model_nmf.components_
    nmf_matrix = m @ h
    x_labels = list(sparse_matrix.index)
    y_labels = list(sparse_matrix.columns)
  
    return x_labels, y_labels, nmf_matrix

# Top 5 most similar documents' indices recommended for document at index 0
def top_10(idx):
    top10 = nmf_matrix[idx].argsort()[-11:][::-1][1:]
    return list(np.array(y_labels)[top10])


def predictions_NMF(nmf_matrix):
    '''
    Desription: makes a dictionary of predictions for all IP addresses
    input: takes an nmf matrix 
    output: outputs a dictionary consisting of the ip as the key, 
    and a list of top 10 recommended documents as the value
    d_predicted = {}
    keys = [list(x_labels)[i] for i in range(nmf_matrix.shape[0])]
    values = [top_10(i) for i in range(len(keys))]
    return dict(zip(keys, values))

def score(df_test, d_predicted):
    '''
    Description: scores based on calculating the number of documents
    correctly predicted to be in the top 10. 
    input: a test df and a dictionary of predicted top 10 
    output:a Precision score
    count = 0
    test = {k:g['accession'].tolist() for k,g in df_test.groupby('ip')}
    for ip,lst in test.items():
        for doc in lst:
            if doc in d_predicted[ip]:
                count+=1
    size = df_test.shape[0]        
    return abs((size-count) / size)
