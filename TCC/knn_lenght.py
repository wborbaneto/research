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

labels = list(['RPM','MAF','Velocidade','%Acelerador','Carga no Motor'])
cl_label = list(['Calma','Normal','Agressiva'])
#labels = list(['RPM','MAF','Speed','Throttle','Engine Load'])

cl3 = pd.read_csv('data/teste/agressiva_teste.csv')
cl2 = pd.read_csv('data/teste/normal_teste.csv')
cl1 = pd.read_csv('data/teste/calma_teste.csv')

a,b,c = cl1.shape[0],cl2.shape[0],cl3.shape[0]
r = [a,b,c]
r = np.min(r)

cl3 = np.array(cl3.values[0:960,:])
cl2 = np.array(cl2.values[0:960,:])
cl1 = np.array(cl1.values[0:960,:])

x = np.r_[cl1,cl2,cl3]
x = np.array(x, dtype=float)
#y = conv.out_b([950,950,950])

x =  (x - np.min(x,0))/(np.max(x,0) - np.min(x,0))
caMax,caMin,caMean,caStd = list(),list(),list(),list()
xx = list()

t_size=5
for n in range(0,int(len(x)/t_size)):
    xx.append(np.mean(x[n*t_size:(n+1)*t_size,:],0))

m = int(len(x)/(3*t_size))
xx = np.array(xx,dtype=float)
y = conv.out_b([m,m,m])
knn = alg.KNearestNeighbors(xx,y)

trainArr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
nnArr = [1, 5, 7, 11, 13, 17]


for nnNumber in nnArr:
    for trainSize in trainArr:
        confArrayList = list()
        for n in range(0,40):
           knn.train(nnNumber, trainSize)
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

caMax_m = np.mean(caMax,1)
caMin_m = np.mean(caMin,1)
caMean_m = np.mean(caMean,1)
caStd_m = np.mean(caStd,1)

print(np.max(caMax))
print(np.min(caMin))
print(np.mean(caStd))
 
plt.figure(1)
for n in range(0, len(nnArr)):
    plt.plot(trainArr,caMax_m[n*9:(n+1)*9])
    
plt.xlabel('Fração dos dados utilizados no Treino')
plt.ylabel('Máxima % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()

plt.figure(2)
for n in range(0, len(nnArr)):
    plt.plot(trainArr,caMin_m[n*9:(n+1)*9])
plt.xlabel('Fração dos dados utilizados no Treino')
plt.ylabel('Mínima % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()

plt.figure(3)
for n in range(0, len(nnArr)):
    plt.plot(trainArr,caMean_m[n*9:(n+1)*9])
plt.xlabel('Fração dos dados utilizados no Treino')
plt.ylabel('Média da % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()

plt.figure(4)
for n in range(0, len(nnArr)):
    plt.plot(trainArr,caStd_m[n*9:(n+1)*9])
plt.xlabel('Fração dos dados utilizados no Treino')
plt.ylabel('Desvio Padrão da % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()
