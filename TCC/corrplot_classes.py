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
cl1 = np.array(cl1.values)

x = np.r_[cl1,cl2,cl3]
y = conv.out_s([a,b,c],['Calma','Normal','Agressiva'])

x =  (x - np.min(x,0))/(np.max(x,0) - np.min(x,0))

xdf = pd.DataFrame(x, columns=labels)

xdf['Classe'] = y 
 
sns.set_palette('bright')
sns.set(font_scale = 1.5)
sns.set_style("ticks")

def corrfunc(x, y, **kws):
    r, _ = stats.pearsonr(x, y)
    ax = plt.gca()
    ax.annotate("r = {:.2f}".format(r),
                xy=(.1, .9), xycoords=ax.transAxes)
    


    
#palette={"Calma":"#1AC938","Normal":"#FFC400","Aggressiva":"#9F4800"}
#blue = #ADB8CB / #0173B2
    
sapoha = xdf[xdf['Classe'] == 'Calma']
g = sns.PairGrid(sapoha, hue = "Classe" )
g.map_offdiag(corrfunc) 
g.map_offdiag(plt.scatter,color = '#1AC938', edgecolor="k", s= 30, marker = "o")
g.map_offdiag(sns.regplot,scatter=False, color="m")
g.add_legend()

sapoha = xdf[xdf['Classe'] == 'Normal']
g1 = sns.PairGrid(sapoha, hue = "Classe" )
g1.map_offdiag(corrfunc) 
g1.map_offdiag(plt.scatter,color = '#FFC400', edgecolor="k", s= 30, marker = "^")
g1.map_offdiag(sns.regplot,scatter=False, color="m")
g1.add_legend()

sapoha = xdf[xdf['Classe'] == 'Agressiva']
g2 = sns.PairGrid(sapoha, hue = "Classe" )
g2.map_offdiag(corrfunc) 
g2.map_offdiag(plt.scatter,color = 'r', edgecolor="k", s= 30, marker = "s")
g2.map_offdiag(sns.regplot,scatter=False, color="m")
g2.add_legend()
#g = sns.PairGrid(xdf, hue="Classe", palette={"Calma":"g","Normal":"y","Aggressiva":"r"},
#                 hue_kws={"marker": ['o', '^', 's']})
#g = g.map_diag(plt.hist, edgecolor="w")
#g = g.map_offdiag(plt.scatter, linewidths=0.05, edgecolor="k", s=30)
#g = g.map_offdiag(plt.scatter, linewidths=0.05, edgecolor="k", s=30)
#g = g.add_legend()
#sns.pairplot(xdf,hue='Class',markers=['o', '^', 's'], palette = {"Calm":"g","Normal":"y","Aggressive":"r"}, plot_kws=dict(edgecolor='k',linewidth=0.05,s=30))
#sns.pairplot(xdf,kind='reg',hue='Classe',markers=['o', '^', 's'], palette = {"Calma":"g","Normal":"y","Aggressiva":"r"})