# K-Means-Clustering
Implementation of K-means algorithm using a toy dataset. It is an unsupervised algorithm that uses two steps to perform clustering of the given data. The following points explain how it is done:
1. Initially a centroid is randomly initialized which is a vector of the same dimensionality as the dataset.
2. Each of the data points is scanned and the distance to all the centroids are evaluated. The centroid that has the minimum distance to the data point is chosen and the data point gets the classs that this centroid belongs to.
3. The Mean of all the data points that belong to the same class are evaluated and this is done for all the centroids(classes).
4. This mean becomes the centroid for the next iteration. After performing this for a given number of iterations until convergence, all those points corresponding to centroid 1 are assigned as belonging to Class-1 and all those points corresponding to centroid 2 are assigned as belonging to Class-2 and so on.

The 1st two points are grouped as 'Cluster assignment step' and the next two points, as 'Move centroid step'. Results are also shown below to illustrate how all the data points in the training data set are categorized before and after applying the clustering algorithm. (Here, only 2 features are considered for the dataset and a binary classification is done. So K=2 and we have two axes to ease up the data visualization part)

Results:
===========
Before Clustering:

![1](https://user-images.githubusercontent.com/30439795/41323545-994c9c88-6e74-11e8-986e-c2f8c615daf0.png)

After Clustering:

![2](https://user-images.githubusercontent.com/30439795/41323561-bab9461e-6e74-11e8-9bb3-6e9217775fa2.png)
