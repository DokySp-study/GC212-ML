
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from matplotlib import pyplot as plt

#
# Load IRIS dataset
iris = datasets.load_iris()
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
X = df.iloc[:, 0:4]

# Instantiate the KMeans models
km = KMeans(n_clusters=4)

# Fit the KMeans model
km.fit_predict(X)

# Calculate Silhoutte Score
score = silhouette_score(X, km.labels_, metric='euclidean')

# Print score
print("\nKMeans(clusters=4) score: ", end="")
print(score)
