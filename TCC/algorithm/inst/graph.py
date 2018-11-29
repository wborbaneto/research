# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 18:03:51 2018

@author: wborbaneto
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the previous results
caMax_m = np.load('results/caMax_m.npy')
caMin_m =np.load('results/caMin_m.npy')
caMean_m =np.load('results/caMean_m.npy')
caStd_m =np.load('results/caStd_m.npy')

# Setting some parameters for the graph
sns.set_palette('bright')
sns.set(font_scale = 1.5)
sns.set_style("ticks")

trainArr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
nnArr = [1, 5, 7, 11, 13, 17]

f = len(trainArr)

plt.figure(1)
for n in range(0, len(nnArr)):
    plt.plot(trainArr,caMax_m[n*f:(n+1)*f], linewidth=5)
    
plt.xlabel('Fração dos dados utilizados no Treino')
plt.ylabel('Máxima % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()

plt.figure(2)
for n in range(0, len(nnArr)):
    plt.plot(trainArr,caMin_m[n*f:(n+1)*f], linewidth=5)
plt.xlabel('Fração dos dados utilizados no Treino')
plt.ylabel('Mínima % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()


plt.figure(3)
for n in range(0, len(nnArr)):
    plt.plot(trainArr,caMean_m[n*f:(n+1)*f], linewidth=5)
plt.xlabel('Fração dos dados utilizados no Treino')
plt.ylabel('Média da % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()


plt.figure(4)
for n in range(0, len(nnArr)):
    plt.plot(trainArr,caStd_m[n*f:(n+1)*f], linewidth=5)
plt.xlabel('Fração dos dados utilizados no Treino')
plt.ylabel('Desvio Padrão da % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()



