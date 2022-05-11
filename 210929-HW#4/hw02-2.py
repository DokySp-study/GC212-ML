
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

# Load IRIS dataset
iris = datasets.load_iris()
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
X = df.iloc[:, 0:4]

# Calculate score of each clusters
range_n_clusters = [2, 3, 4, 5, 6]
silhouette_avg = []
for num_clusters in range_n_clusters:
    # initialize kmeans
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)
    cluster_labels = kmeans.labels_
    # silhouette score
    silhouette_avg.append(silhouette_score(X, cluster_labels))

# Plot the result of score of clusters
ax=plt.axes()
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

plt.plot(range_n_clusters,silhouette_avg,'bx-')
plt.xlabel('Values of K')
plt.ylabel('Silhouette score')
plt.title('Silhouette analysis For Optimal k')
plt.show()

# Find Optimal number of cluster and print the result
max = -1.0
maxIdx = 0
for i in range(0, len(silhouette_avg)):
    if max < silhouette_avg[i]:
        max = silhouette_avg[i]
        maxIdx = range_n_clusters[i]

print("\nOptimal number of clusters: ", end="")
print(maxIdx)
print("Score of clusters: ", end="")
print(max)