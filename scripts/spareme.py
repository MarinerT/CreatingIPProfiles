#!/usr/bin/env/python3

import numpy as np
import pandas as pd

def preprocessing2(csv):
    df = pd.read_csv(csv)
    df = df.set_index('datetime')
    df = df.drop(['ip_ccount','doc_ccount', 'date', 'time', 'datetime.1'],axis=1)
    df['toDoc'] = df.groupby('ip')['accession'].shift(-1).fillna(0)
    return df

def calc_sparsity(df):
    return np.sum(df)/np.prod(df.shape)

def sparsity_matrix(col1,col2):
    df_spar = pd.crosstab(col1, col2,dropna=False)
    drop_list =[]
    for x in df_spar.index.unique():
        if x not in df_spar.columns.unique():
            drop_list.append(x)
    return df_spar.drop(drop_list).drop(0, axis=1)

def create_sparsity_matrix(csv):
    df = preprocessing2(csv)
    return sparsity_matrix(df.accession, df.toDoc)
