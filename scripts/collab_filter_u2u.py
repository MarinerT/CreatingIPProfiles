#!/usr/bin/env/python3

import numpy as np
import pandas as pd
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist
from scripts.cleaner import logFile
from scripts.sparseme import sparse_maker

#create the df sparse matrix

file = '~/SageMaker/CreatingIPProfiles/data/log20101010.csv'
log = logFile(file)

df = log.extract()

sparse_matrix = sparse_maker(df)

# create our pairwise distance matrix
pairwise = pd.DataFrame(
    squareform(pdist(sparse_matrix, metric='cosine')),
    columns = sparse_matrix.index,
    index = sparse_matrix.index
)

# move to long form
long_form = pairwise.unstack()

# rename columns and turn into a dataframe
long_form.index.rename(['ip', 'ip2'], inplace=True)
long_form = long_form.to_frame('cosine distance').reset_index()


#Cosine Similarity
long_form.head(10)

#How many different numbers are there? Did it return something other than 0 and 1?
len(long_form['cosine distance'].unique())

def count_cosine_variations(df):
    d_cosines = {}
    for cosine in df['cosine distance']:
        if cosine in d_cosines:
            d_cosines[cosine]+=1
        else:
            d_cosines[cosine] = 1
    return d_cosines

import matplotlib.pyplot as plt

%matplotlib inline


d_cosines = count_cosine_variations(long_form)

keys = d_cosines.keys()
vals = d_cosines.values()

#Graphing the distribution of the cosine similarities
plt.scatter(keys, np.divide(list(vals), sum(vals)), label="Real distribution")

plt.ylim(0,1)
plt.ylabel ('Percentage')
plt.xlabel ('Significant number')
plt.xticks(np.arange(0, 1, step=0.2))

plt.show()
