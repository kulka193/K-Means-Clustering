# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 18:45:41 2018

@author: bharg
"""

import numpy as np
import matplotlib.pyplot as plt

def data_gen(m):
    x1=1+0.1*np.random.randn(int(m/2),2)
    x2=1+0.1*np.random.randn(int(m/2),2)
    x=np.vstack((x1,x2))
    randvec=np.random.randint(0,high=len(x)-1,size=(m,1))
    Xs=x[randvec[:,0]]
    return Xs


def plot_data(Xs,apply_kmeans=True):
    if not apply_kmeans:
        class1=plt.scatter(Xs[I1,0],Xs[I1,1],c='r')
        class2=plt.scatter(Xs[I2,0],Xs[I2,1],c='b')
        plt.legend((class1,class2),('Class 1','Class 2'),loc='lower left')
        plt.grid()
        plt.show()
    else:
        plt.scatter(Xs[:,0],Xs[:,1])
        plt.grid()
        plt.show()


def init_centroids(Xs):
    rand_plt1=np.random.randint(0,high=len(Xs)-1,size=1)
    rand_plt2=np.random.randint(0,high=len(Xs)-1,size=1)
    cc1=Xs[rand_plt1,:]
    cc2=Xs[rand_plt2,:]
    return (cc1,cc2)


def cluster_assign(Xs,cc1,cc2):
    I1,I2=[],[]
    m=Xs.shape[0]
    for i in range(m):
        dist_to_cluster=[np.linalg.norm(Xs[i,:]-cc1)**2,np.linalg.norm(Xs[i,:]-cc2)**2]
        idx=dist_to_cluster.index(min(dist_to_cluster))
        if idx==0:
            I1.append(i)
        elif idx==1:
            I2.append(i)
    return I1,I2


if __name__=="__main__":
    num_data=int(input('Enter the number of data points: '))
    K=2
    data=data_gen(num_data)
    ret=plot_data(data)
    [centroid1,centroid2]=init_centroids(data)
    num_iters=1000
    global I1,I2
    for _ in range(num_iters):
        I1,I2=cluster_assign(data,centroid1,centroid2)
        centroid1=np.mean(data[I1],axis=1,keepdims=True)
        centroid2=np.mean(data[I2],axis=1,keepdims=True)
    plot_data(data,apply_kmeans=False)
    



        