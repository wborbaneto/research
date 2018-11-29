# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 10:22:26 2018

@author: wborbaneto
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import algorithm as alg
import pyconv as conv
import pickle
from datetime import datetime


#Statements


labels = list(['RPM','MAF','Velocidade','%Acelerador','Carga no Motor'])
cl_label = list(['Calma','Normal','Agressiva'])
#labels = list(['RPM','MAF','Speed','Throttle','Engine Load'])

cl3 = pd.read_csv('data/teste/agressiva_teste.csv')
cl2 = pd.read_csv('data/teste/normal_teste.csv')
cl1 = pd.read_csv('data/teste/calma_teste.csv')

a,b,c = cl1.shape[0],cl2.shape[0],cl3.shape[0]
r = [a,b,c]
r = np.min(r)
cl3 = np.array(cl3.values)
cl2 = np.array(cl2.values)
cl1 = np.array(cl1.values)


x = np.r_[cl1,cl2,cl3]
x = np.array(x, dtype=float)
y = conv.out_b([a,b,c])

x =  (x - np.min(x,0))/(np.max(x,0) - np.min(x,0))
caMax,caMin,caMean,caStd = list(),list(),list(),list()


 
knn = alg.KNearestNeighbors(x,y)

trainArr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
nnArr = [1]
time = list()

lenghtArr = [1, 2, 3, 4, 5, 6, 8, 10]

        
# for t_size in lenghtArr:
#     xx = x
#     m = int(len(x)/(3*t_size))
#     xx = np.array(xx,dtype=float)
#     xx = xx.reshape(int(len(x)/t_size),5*t_size)
#     y = conv.out_b([m,m,m])
#     knn = alg.KNearestNeighbors(xx,y)
#     confArrayList = list()
#     start=datetime.now()
#     for n in range(0,100):
#        knn.train(1, 0.8)
#        confArrayList.append(knn.confArray)
#     time.append(datetime.now()-start)    
#     cal = np.array(confArrayList) 
#     caMax.append(np.diag(np.max(cal,0)))
#     caMin.append(np.diag(np.min(cal,0)))
#     caMean.append(np.diag(np.mean(cal,0)))
#     caStd.append(np.diag(np.std(cal,0)))
    

knn = alg.KNearestNeighbors(x,y)
confArrayList = list()
start=datetime.now()
for n in range(0,100):
   knn.train(1, 0.8)
   confArrayList.append(knn.confArray)
   time.append(datetime.now()-start)    
   cal = np.array(confArrayList) 
   caMax.append(np.diag(np.max(cal,0)))
   caMin.append(np.diag(np.min(cal,0)))
   caMean.append(np.diag(np.mean(cal,0)))
   caStd.append(np.diag(np.std(cal,0)))
    
# for nnNumber in nnArr:
#     start=datetime.now()
#     confArrayList = list()
    
#     for n in range(0,100):
#        knn.train(1, 0.8, dist='eDist')
#        confArrayList.append(knn.confArray)
       
#     time.append((datetime.now()-start).timestamp)   
#     cal = np.array(confArrayList) 
#     caMax.append(np.diag(np.max(cal,0)))
#     caMin.append(np.diag(np.min(cal,0)))
#     caMean.append(np.diag(np.mean(cal,0)))
#     caStd.append(np.diag(np.std(cal,0)))
        
caMax = np.array(caMax)
caMin = np.array(caMin)
caMean = np.array(caMean)
caStd = np.array(caStd)

caMax_m = np.mean(caMax,1)
caMin_m = np.mean(caMin,1)
caMean_m = np.mean(caMean,1)
caStd_m = np.mean(caStd,1)

print(np.max(caMax))
print(np.min(caMin))
print(np.mean(caStd))
 

sns.set_palette('bright')
sns.set(font_scale = 1.5)
sns.set_style("ticks")

# name = 'Custo computacional'
# time = [20.193, 20.160, 20.182, 20.337, 20.811, 20.470]
# plt.figure(1)
# plt.plot(nnArr,time, linewidth=5)
# plt.xlabel('Número de vizinhos mais próximos')
# plt.ylabel('Tempo (s)')
# plt.legend([name])
# plt.grid()


name = 'Custo computacional'
time = [20.193, 4.758, 2.381, 1.312, 0.881,0.6456,0.413, 0.312 ]
plt.figure(1)
plt.plot(lenghtArr,time, linewidth=5)
#plt.xlabel('Número de vizinhos mais próximos')
#plt.ylabel('Tempo (s)')
#plt.legend([name])
plt.grid()
    
name = 'Custo computacional'
time = [20.152, 5.615, 2.820, 2.009 ,1.389, 1.077, 0.752,0.5917]
#plt.figure(1)
plt.plot(lenghtArr,time, linewidth=5)
plt.xlabel('Número de vetores na Janela Temporal')
plt.ylabel('Tempo (s)')
plt.legend(['Centroide','Janela'])
#plt.grid()

