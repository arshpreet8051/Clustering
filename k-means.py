# K-Means Clustering

# Importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing the dataset

dataset = pd.read_csv('Mall_Customers.csv')
x = dataset.iloc[:,[3,4]].values # only annual income and spending score col 
# Using the elbow method to find the optimal number of clusters

from sklearn.cluster import KMeans
wcss = [] #within cluster sum square
for i in range(1,11): # 1 to 10 clusters
  kmeans = KMeans(n_clusters=i,init='k-means++',random_state=42)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_) # using inertia_ attribute to get wcss score

# plotting graph tp find the "kink"
plt.plot(range(1,11),wcss)
plt.title("Elbow mwthod implementation")
plt.xlabel("No of clusters")
plt.ylabel("WCSS")
plt.show()

# Training the K-Means model on the dataset

kmeans = KMeans(n_clusters=5,init='k-means++',random_state=42)
y_means = kmeans.fit_predict(x)
# ymeans is for alloting category no 

print(y_means)

# Visualising the clusters

#plotting categories

plt.scatter(x[y_means==0,0],x[y_means==0,1],label="Cluster : 1",s=100,c='red') # category 1
plt.scatter(x[y_means==1,0],x[y_means==1,1],label="Cluster : 2",s=100,c='blue') # category 2
plt.scatter(x[y_means==2,0],x[y_means==2,1],label="Cluster : 3",s=100,c='green') # category 3
plt.scatter(x[y_means==3,0],x[y_means==3,1],label="Cluster : 4",s=100,c='cyan') # category 4
plt.scatter(x[y_means==4,0],x[y_means==4,1],label="Cluster : 5",s=100,c='yellow') # category 5

# plotting centroids

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],label="Centroids",s=90,c='black')

# other plotting details

plt.title('K-means clustering')
plt.xlabel('Spending metrices score')
plt.ylabel('Annual income (k$)')
plt.legend()
plt.show()
