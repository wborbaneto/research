# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:41:26 2018

@author: AHCI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import algorithm as alg
import pyconv as conv
from scipy import stats

labels = list(['RPM','MAF','Velocidade','%Acelerador','Carga no Motor'])
#labels = list(['RPM','MAF','Speed','Throttle','Engine Load'])
cl3 = pd.read_csv('data/teste/agressiva_teste.csv')
cl2 = pd.read_csv('data/teste/normal_teste.csv')
cl1 = pd.read_csv('data/teste/calma_teste.csv')

a,b,c = cl1.shape[0],cl2.shape[0],cl3.shape[0]
r = [a,b,c]
r = np.min(r)

cl3 = np.array(cl3.values)
cl2 = np.array(cl2.values)
cl1 = np.array(cl1.values[0:999,:])

x = np.r_[cl1,cl2,cl3]
y = conv.out_s([a,b,c],['Calma','Normal','Aggressiva'])

cl1 =  (cl1 - np.min(cl1,0))/(np.max(cl1,0) - np.min(cl1,0))
cl2 =  (cl2 - np.min(cl2,0))/(np.max(cl2,0) - np.min(cl2,0))
cl3 =  (cl3 - np.min(cl3,0))/(np.max(cl3,0) - np.min(cl3,0))

a = 0
b = 999
c = 0
d = 4
t = 1
cl1df = pd.DataFrame(cl1[a:b,c:d], columns = labels[c:d])
cl2df = pd.DataFrame(cl2[a:b,c:d], columns = labels[c:d])
cl3df = pd.DataFrame(cl3[a:b,c:d], columns = labels[c:d])

sns.set_palette('bright')
sns.set(font_scale = 1.5)
sns.set_style("ticks")

x = np.arange(0,b)

plt.figure(1)
#sns.lineplot(data = cl1df, hue=['RPM','MAF','Velocidade','%Acelerador'],size=['2','2','2','3'])
g1 = plt.plot(x, cl1[:,1],'g', x,cl3[:,1],'r-',)
plt.grid()
plt.setp(g1[0],  linewidth=4)
plt.setp(g1[1],  linewidth=4)

plt.xlabel('Tempo (ds)')
plt.ylabel(labels[1])
plt.legend(['Calma','Agressiva'])

plt.figure(2)
ym1 = np.ma.masked_where(cl3[0:b,t] >= cl1[0:b,t], cl3[0:b,t])
ym2 = np.ma.masked_where(~(np.array(cl3[0:b,t] < cl2[0:b,t],dtype=bool) & np.array(cl3[0:b,t] > cl1[0:b,t],dtype=bool)), cl3[0:b,t])

g = plt.plot(x,cl3[0:b,t],'r',x,ym2,'y',x,ym1,'g')

plt.setp(g[0],  linewidth=6)
plt.setp(g[1],  linewidth=10)
plt.setp(g[2],  linewidth=6)
    
plt.xlabel('Tempo (ds)')
plt.ylabel(labels[t])
plt.grid()
plt.legend(['Aggressiva', 'Normal','Calma'])

