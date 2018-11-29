# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 18:03:51 2018

@author: wborbaneto
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.signal import lfilter

# Loading the previous results
caMax_m = np.load('results/caMax_m_nn1_old.npy')
caMin_m =np.load('results/caMin_m_nn1_old.npy')
caMean_m =np.load('results/caMean_m_nn1_old.npy')
caStd_m =np.load('results/caStd_m_nn1_old.npy')


# Setting some parameters for the graph
sns.set_palette('bright')
sns.set(font_scale = 1.5)
sns.set_style("ticks")

lenghtArr = np.linspace(1,80,80,dtype=int)
nnArr = [1]  

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

plt.plot(lenghtArr,caMean_m[0*f:(0+1)*f], linewidth=5) 
plt.xticks(np.arange(0, 240, step=5))
plt.grid()