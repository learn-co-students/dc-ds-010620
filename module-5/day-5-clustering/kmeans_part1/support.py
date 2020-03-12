## let's play with cluster_std and try to find number of clusters

np.random.seed(110119)

X, y = make_blobs(n_samples = 700, n_features = 2, centers = np.array([[-10, -20],
                                                                       [-5, -15],
                                                                       [-2, -9],
                                                                       [5, 12],
                                                                       [7, 17]
                                                                      ]), cluster_std=5 )

import pickle
object_blobs_1 = [X,y]
file_blobs_1 = open('blobs_1.obj', 'wb')
pickle.dump(object_blobs_1, file_blobs_1)


## let's instantiate kmeans algorithm
## don't forget to check its parameters
k_means = KMeans(n_clusters= 5)

# dont forget to fit the model!
k_means.fit(X)

## we make a prediction for each point
y_hat = k_means.predict(X)

## we can access the coordinates of the cluster centers by cluster_centers_ method
cl_centers = k_means.cluster_centers_

print(cl_centers)
## note that the colors are different - Is this a problem?
plt.scatter(X[:,0], X[:,1], c = y_hat, s = 25)


## also let's mark the cluster centers too.
plt.scatter(cl_centers[:, 0], cl_centers[:, 1], c='black', s=100);
