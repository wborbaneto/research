# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 17:27:36 2018

@author: AHCI
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import algorithm as alg
import seaborn as sns
import pyconv as conv



#'Consumo','RPM','MAF','Velocidade','Aceleracao','CargaMotor'
#labels = list(['RPM','MAF','Speed','Throttle'])
labels = list(['RPM','MAF','Velocidade','Aceleracao'])

cl3 = pd.read_csv('data/teste/agressiva_teste.csv')
cl2 = pd.read_csv('data/teste/normal_teste.csv')
cl1 = pd.read_csv('data/teste/calma_teste.csv')

irisdf = pd.read_csv('data/iris.csv')
iris = np.array(irisdf.values[:,0:4],dtype='float64')

a,b,c = cl1.shape[0],cl2.shape[0],cl3.shape[0]
r = [a,b,c]
r = np.min(r)

#a,b,c = 50,50,50
#cl1 = iris[0:a,:]
#cl2 = iris[a:a+b,:]
#cl3 = iris[a+b:a+b+c,:]

cl3 = np.array(cl3.values[:,0:4])
cl2 = np.array(cl2.values[:,0:4])
cl1 = np.array(cl1.values[:,0:4])


cl3 =cl3[0:960,:]
cl2 = cl2[0:960,:]
cl1 = cl1[0:960,:]

x = np.r_[cl1,cl2,cl3]
y = conv.out_b([a,b,c])

x =  (x - np.min(x,0))/(np.max(x,0) - np.min(x,0))


t_size=10

xx=list()
for n in range(0,int(len(x)/t_size)):
    xx.append(np.mean(x[n*t_size:(n+1)*t_size,0:5],0))

m = int(len(x)/(3*t_size))
xx = np.array(xx,dtype=float)
y = conv.out_b([m,m,m])
dist = 'eDist'
    
km = alg.kmeans(xx,y)  
centroid,error = km.train(1,3,randomize=0,dist=dist)

print(centroid)
p1 = 2
p2 = 3

# plt.figure(1)
# plt.plot(x[0:a,p1],x[0:a,p2],'go',markersize=4)
# plt.plot(x[a:a+b,p1],x[a:a+b,p2],'y^',markersize=4)
# plt.plot(x[a+b:a+b+c,p1],x[a+b:a+b+c,p2],'rs',markersize=4)
# plt.plot(centroid[:,p1],centroid[:,p2],'bX',markersize=10)
# plt.xlabel(labels[p1]),plt.ylabel(labels[p2])
# if dist == 'eDist': plt.title('K-means (eDist) Input')
# else: plt.title('K-means (mDist) Input')

# dep = km.winners
# plt.figure(2)    
# xcl1,xcl2,xcl3 = x[(km.winners==0).ravel()],x[(km.winners==1).ravel()],x[(km.winners==2).ravel()]
# plt.plot(xcl1[:,p1],xcl1[:,p2],'go',markersize=4)
# plt.plot(xcl2[:,p1],xcl2[:,p2],'y^',markersize=4)
# plt.plot(xcl3[:,p1],xcl3[:,p2],'rs',markersize=4)
# plt.plot(centroid[:,p1],centroid[:,p2],'bX',markersize=10)
# plt.xlabel(labels[p1]),plt.ylabel(labels[p2])
# if dist == 'eDist': plt.title('K-means (eDist) Output')
# else: plt.title('K-means (mDist) Output')

xxdf = pd.DataFrame(xx)
xdf = pd.DataFrame(x, columns=labels)
xxdf['Classe'] = conv.dec2str(km.winners,['Calma','Normal','Agressiva'])
#g1=sns.pairplot(xdf,hue='Class',markers=['o', '^', 's'], palette = {"Calm":"g","Normal":"y","Aggressive":"r"}, plot_kws=dict(edgecolor='k',linewidth=0,s=30))
#g2=sns.pairplot(xdf,kind='reg',hue='Class',markers=['o', '^', 's'], palette = {"Calm":"g","Normal":"y","Aggressive":"r"}, 
#             plot_kws={'scatter_kws':{'linewidth':0,'s':30}})

sns.set(font_scale = 1.5)
sns.set_style("ticks")

xxdf['Classe'] = conv.bin2str(y,['Calma','Normal','Agressiva'])
g = sns.PairGrid(xxdf, hue = "Classe", hue_kws={"marker": ["o", "^", "s"]}, palette = {"Calma":"#1AC938","Normal":"#FFC400","Agressiva":"r"})
g.map_offdiag(plt.scatter,linewidth=0.3, edgecolor="k", s= 30, marker = "s")   
g.map_diag(sns.kdeplot,shade=True)
g.add_legend()

#g3=sns.pairplot(xdf,hue='Classe',markers=['o', '^', 's'], palette = {"Calma":"#1AC938","Normal":"#FFC400","Agressiva":"#9F4800"}, plot_kws=dict(edgecolor='k',s=30))
#g4=sns.pairplot(xdf,kind='reg',hue='Class',markers=['o', '^', 's'], palette = {"Calm":"g","Normal":"y","Aggressive":"r"}, 
#             plot_kws={'scatter_kws':{'linewidth':0,'s':30}})

#g1.fig.suptitle('K-means ('+dist+') Output')
#g2.fig.suptitle('K-means ('+dist+') Regressed Output')
#g3.fig.suptitle('K-means ('+dist+') Input')
#g4.fig.suptitle('K-means ('+dist+') Regressed Input')

print(np.mean(x[0:a,:],0))
print(np.mean(x[a:a+b,:],0))
print(np.mean(x[a+b:a+b+c,:],0))

