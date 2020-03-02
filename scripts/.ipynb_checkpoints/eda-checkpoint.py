#!/usr/bin/env/python3

#import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import stats
import statsmodels.api as sm
from sklearn.metrics import accuracy_score
import seaborn as sns
from scripts.cleaner import logFile

%matplotlib inline

file = '~/SageMaker/CreatingIPProfiles/log20101010.csv'

log = logFile(file)

df = log.extract()

df_original = log.transformer(df)

def filterer(df, iphitsmax=200, iphitsmin=5, dochitsmax=200, dochitsmin=30):
    return df.query('@iphitsmax > ip_total_count > @iphitsmin and @dochitsmax > doc_total_count > @dochitsmin').drop(['date', 'time', 'datetime', 'ip_ccount', 'doc_ccount'],axis=1)

df_filtered = filterer(df_original)

def stats(df_original, df_filtered):
    df_original = df_original.drop(['ip_ccount', 'doc_ccount'],axis=1)
    print(df_original.describe())
    print(df_filtered.describe())
    unique_docs_original = len(list(df_original.accession.unique()))
    unique_ips_original = len(list(df_original.ip.unique()))
    unique_docs_filtered = len(list(df_filtered.accession.unique()))
    unique_ips_filtered = len(list(df_filtered.ip.unique()))
    print("\nEvents: {}\nSample Size: {}\nPercent Reduction: {:2f}"
          .format(df_original.ip.count(), df_filtered.ip.count(), 1-(df_filtered.ip.count()/df_original.ip.count())))
    print("Documents in Original: {}\nDocuments in Sample: {}\nPercent Reduction: {:2f}"
          .format(unique_docs_original, unique_docs_filtered, 1-(unique_docs_filtered/unique_docs_original)))
    print("IPs in Original: {}\nIPs in Sample: {}\nPercent Reduction: {:2f}"
          .format(unique_ips_original, unique_ips_filtered, 1-(unique_ips_filtered/unique_ips_original)))

stats(df_original, df_filtered)

#plot count for IPs

plt.hist(df_original.ip_total_count)
plt.title("IP Counts in Original", fontsize=20)
plt.xlabel("Unique IP Address Bins")
plt.ylabel("Count of Unique IP Addresses")

plt.hist(df_filtered.ip_total_count, alpha=0.5, label='Sample')
plt.title("IP Counts in Sample", fontsize=20)
plt.xlabel("Unique IP Address Bins")
plt.ylabel("Count of Unique IP Addresses")
plt.show()

plt.hist(df_original.doc_total_count, alpha=0.5)
plt.title("Document Counts in Original", fontsize=20)
plt.xlabel("Unique Documents Address Bins")
plt.ylabel("Count of Unique Documents Addresses")
plt.show()

plt.hist(df_filtered.doc_total_count, alpha=0.5, label='Sample')
plt.title("Document Counts in Sample", fontsize=20)
plt.xlabel("Unique Documents Address Bins")
plt.ylabel("Count of Unique Documents Addresses")
plt.show()

def savetocsv(df, title):
    df = df.drop(['doc_total_count','ip_total_count'],axis=1)
    df.to_csv(title)

savetocsv(df_filtered, 'df_filtered.csv')
