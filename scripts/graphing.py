#!/usr/bin/env/python3

#import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc
import networkx as nx
import nxpd as nxpd
import community as comm
import graph_tools as gt
from itertools import product

plt.style.use('ggplot')

csv = 'df_filtered.csv'

#create G
def create_G(csv):
    sparsemat = create_sparsity_matrix(csv)
    features = sparsemat.columns
    g_mat = np.array(sparsemat)
    G = nx.Graph(g_mat)
    return features, G

#Create the features array, get info
features, G = create_G(csv)
print(nx.info(G))

#plot_nodes
def plot_Gnodes(G):
    G.graph['rankdir'] = 'LR'
    return nxpd.draw(G, show='ipynb')

plot_Gnodes(G)

#plot_betweeness
def plot_betweenness(G):
    pos = nx.spring_layout(G)
    betCent = nx.betweenness_centrality(G, normalized=True, endpoints=True)
    node_color = [20000.0 * G.degree(v) for v in G]
    node_size =  [v * 10000 for v in betCent.values()]
    plt.figure(figsize=(20,20))
    nx.draw_networkx(G, pos=pos, with_labels=False,
                 node_color=node_color,
                 node_size=node_size )
    plt.axis('off')

plot_betweenness(G)

#top5 Influencers
def top5(G):
    betCent = nx.betweenness_centrality(G, normalized=True, endpoints=True)
    top5centrality = sorted(betCent, key=betCent.get, reverse=True)[:5]
    return features[top5centrality]

top5(G)

