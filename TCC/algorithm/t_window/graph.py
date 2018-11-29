# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 18:03:51 2018

@author: wborbaneto
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import savgol_filter


# Loading the previous results
caMax_m = np.load('results/caMax_m.npy')
caMin_m =np.load('results/caMin_m.npy')
caMean_m =np.load('results/caMean_m.npy')
caStd_m =np.load('results/caStd_m.npy')

caMean_m = savgol_filter(caMean_m, 7, 2)
# Setting some parameters for the graph
sns.set_palette('bright')
sns.set(font_scale = 1.5)
sns.set_style("ticks")

trainArr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
lenghtArr = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 16, 20, 24, 30, 32, 40, 48, 60, 64, 80, 96, 120, 160]
lenghtArr = np.linspace(1,240,49,dtype=int)
nnArr = [1, 5, 7, 11, 13, 17]

f = len(lenghtArr)

plt.figure(1)
for n in range(0, len(nnArr)):
    plt.plot(lenghtArr,caMax_m[n*f:(n+1)*f], linewidth=5)
    
plt.xlabel('Tamanho da janela temporal')
plt.ylabel('Máxima % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()

plt.figure(2)
for n in range(0, len(nnArr)):
    plt.plot(lenghtArr,caMin_m[n*f:(n+1)*f], linewidth=5)
plt.xlabel('Tamanho da janela temporal')
plt.ylabel('Mínima % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()


plt.figure(3)
for n in range(0, len(nnArr)):
    plt.plot(lenghtArr,caMean_m[n*f:(n+1)*f], linewidth=5)
plt.xlabel('Tamanho da janela temporal')
plt.ylabel('Média da % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()


plt.figure(4)
for n in range(0, len(nnArr)):
    plt.plot(lenghtArr,caStd_m[n*f:(n+1)*f], linewidth=5)
plt.xlabel('Tamanho da janela temporal')
plt.ylabel('Desvio Padrão da % Correta de Classificação')
plt.legend(["K = "+str(n) for n in nnArr])
plt.grid()


oie = caMean_m[0*f:(0+1)*f]
idx = (-oie.T).argsort()
lenghtArr[idx]

