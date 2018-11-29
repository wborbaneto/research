# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 11:24:23 2018

@author: wborbaneto
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyconv as conv
import algorithm as alg
from datetime import datetime

# Labels for the features and classes (pt-br). 
labels = list(['RPM','MAF','Velocidade','%Acelerador','Carga no Motor'])
cl_label = list(['Calma','Normal','Agressiva'])

# Labels for the features and classes (en). 
# labels = list(['RPM','MAF','Speed','%Throotle','Engine Load'])
# cl_label = list(['Calm','Mild','Aggressive'])

# Importing the data as a DataFrame (See more in https://pandas.pydata.org/)
cl1 = pd.read_csv('data/cl1.csv',names=labels)
cl2 = pd.read_csv('data/cl2.csv',names=labels)
cl3 = pd.read_csv('data/cl3.csv',names=labels)

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
# Our output using a proprietary function (See pyconv.py).
y = conv.out_b([a,b,c])

# Test parameters. Desired train ration an Nearest Neighbors are altered here.
nnArr = [1, 5, 7, 11, 13, 17]
trainSize = 0.7

# Initializing our algorithm (See algorithm.py).
knn = alg.KNearestNeighbors(x,y)
time = list()

# For loop to calculate time
for nnNumber in nnArr:
    start = datetime.now()
    knn.train(nnNumber, trainSize, dist='eDist')
    time.append((datetime.now()-start).total_seconds())

print("Finished! Confusion Matrix:")
print(knn.confArray)
time = np.array(time,dtype=float)
# Setting some parameters for the graph
sns.set_palette('bright')
sns.set(font_scale = 1.5)
sns.set_style("ticks")

name = 'Custo computacional'
plt.figure(1)
plt.plot(nnArr,100*time, linewidth=5)
plt.xlabel('Número de Vizinhos mais próximos')
plt.ylabel('Tempo (s)')
plt.grid()


 

