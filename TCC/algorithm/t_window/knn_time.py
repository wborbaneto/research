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

# Our output using a proprietary function (See pyconv.py).
y = conv.out_b([a,b,c])

# Overwrite Results?
ovrw = 1

# Test parameters. Desired train ration an Nearest Neighbors are altered here.
lenghtArr = [1,2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 20, 24, 30, 32, 40, 48, 60, 64, 80, 96, 120, 160, 192, 240, 320]
trainSize = 0.7
numC = 3
nnNumber = 17

# Initializing our algorithm (See algorithm.py).
(m,n) = x.shape
knn = alg.KNearestNeighbors(x,y)
time = list()

# For loop to calculate KNN based on trainArr and nnArr
for t_size in lenghtArr:
    # A buffer.
    xx = x
    # Number of groups that will ber created.
    ng = int(len(x)/(numC*t_size))
    xx = np.array(xx,dtype=float)
    # Reshaping our input to join our group vectors.
    xx = xx.reshape(int(len(x)/t_size),5*t_size)
    # Reshaping y to the new expected output
    y = conv.out_b([ng,ng,ng])
    # Initializing our KNN with the new input xx.
    knn = alg.KNearestNeighbors(xx,y)
 
    confArrayList = list()
    # Common loop from previous analysis.
    start = datetime.now()
    knn.train(nnNumber, trainSize, randomize=1)
    time.append((datetime.now()-start).total_seconds())
    confArrayList.append(knn.confArray)

print("Finished! Confusion Matrix:")
print(knn.confArray)

# Setting some parameters for the graph
sns.set_palette('bright')
sns.set(font_scale = 1.5)
sns.set_style("ticks")

name = 'Custo computacional'
plt.figure(1)
plt.plot(lenghtArr,time, linewidth=5)
plt.xlabel('Tamanho da janela temporal (t)')
plt.ylabel('Tempo (s)')
plt.grid()




 

