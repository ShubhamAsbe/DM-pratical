# -*- coding: utf-8 -*-
"""Clustering_k_means.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J96f-WQRn1wLwv_9dfpQM-lHSQRMoK9N
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

customers_data = pd.read_csv("Mall_Customers.csv")

customers_data = customers_data.drop('CustomerID', axis=1)

from sklearn.preprocessing import LabelEncoder

encode = LabelEncoder()
encoded_sex = encode.fit_transform(customers_data.iloc[:, 0])
print(encoded_sex)

customers_data['Gender'] = encoded_sex

customers_data.head()

customers_data.columns

from sklearn.decomposition import PCA
pca_reducer = PCA(n_components=2)
reduced_data = pca_reducer.fit_transform(customers_data)

reduced_data.shape

reduced_data

from sklearn.cluster import KMeans

km = KMeans(n_clusters=5)

cluster = km.fit(reduced_data)

plt.scatter(reduced_data[:, 0], reduced_data[:, 1], label='Datapoints')
plt.scatter(cluster.cluster_centers_[:, 0], cluster.cluster_centers_[:, 1], label='Clusters')
plt.title("Sklearn version of KMeans")
plt.legend()
plt.show()