# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 11:24:23 2018

@author: wborbaneto
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyconv as conv
import algorithm as alg

# Labels for the features and classes (pt-br). 
labels = list(['RPM','MAF','Velocidade','%Acelerador','Carga no Motor'])
cl_label = list(['Calma','Normal','Agressiva'])

# Labels for the features and classes (en). 
# labels = list(['RPM','MAF','Speed','%Throotle','Engine Load'])
# cl_label = list(['Calm','Mild','Aggressive'])

# Importing the data as a DataFrame (See more in https://pandas.pydata.org/)
cl1 = pd.read_csv('data/cl1_.csv',names=labels)
cl2 = pd.read_csv('data/cl2_.csv',names=labels)
cl3 = pd.read_csv('data/cl3_.csv',names=labels)

# Getting data size. You may want to concatenate your data to make sure that
# all classes have equal size. To do this, use the 'r' variable.
a,b,c = cl1.shape[0],cl2.shape[0],cl3.shape[0]
r = [a,b,c]
r = np.min(r)

# Only the values from the DF are useful in this analysis. When plotting a 
# matrix graph, the DF come in handy.
cl1 = cl1.values[:r,:]
cl2 = cl2.values[:r,:]
cl3 = cl3.values[:r,:]

# Our input
x = np.r_[cl1 ,cl2,cl3]
x = np.array(x, dtype=float)
x = conv.normalize(x)

# Our output using a proprietary function (See pyconv.py).
y = conv.out_b([a,b,c])

# Test parameters. Desired train ration an Nearest Neighbors are altered here.
trainArr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
nnArr = [1, 5, 7, 11, 13, 17]
testN = 30

# Overwrite Results?
ovrw = 1

# Initializing our algorithm (See algorithm.py).
knn = alg.KNearestNeighbors(x,y)
caMax,caMin,caMean,caStd = list(),list(),list(),list()

# For loop to calculate KNN based on trainArr and nnArr
for nnNumber in nnArr:
    for trainSize in trainArr:
        confArrayList = list()
        for n in range(0,testN):
           knn.train(nnNumber, trainSize, dist='eDist')
           confArrayList.append(knn.confArray)
           
        cal = np.array(confArrayList) 
        caMax.append(np.diag(np.max(cal,0)))
        caMin.append(np.diag(np.min(cal,0)))
        caMean.append(np.diag(np.mean(cal,0)))
        caStd.append(np.diag(np.std(cal,0)))
 
caMax = np.array(caMax)
caMin = np.array(caMin)
caMean = np.array(caMean)
caStd = np.array(caStd)

# Arrays that contain all the results
caMax_m = np.mean(caMax,1)
caMin_m = np.mean(caMin,1)
caMean_m = np.mean(caMean,1)
caStd_m = np.mean(caStd,1)

print("Finished!")

if ovrw:
    np.save('results/caMax_m.npy', caMax_m)
    np.save('results/caMin_m.npy', caMin_m)
    np.save('results/caMean_m.npy', caMean_m)
    np.save('results/caStd_m.npy', caStd_m)
    


 

