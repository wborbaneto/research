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
y = conv.out_s([a,b,c],['Calma','Normal','Aggressiva'])

cl1 =  (cl1 - np.min(cl1,0))/(np.max(cl1,0) - np.min(cl1,0))

cl1df = pd.DataFrame(cl1.T)
cl1df['Tipo'] = labels 
sns.set_palette('bright')
sns.set(font_scale = 1.5)
sns.set_style("ticks")



def corrfunc(x, y, **kws):
    r, _ = stats.pearsonr(x, y)
    ax = plt.gca()
    ax.annotate("r = {:.2f}".format(r),
                xy=(.1, .9), xycoords=ax.transAxes)

g = sns.PairGrid(cl1df, hue = "Tipo")
#g.map_offdiag(corrfunc)
#g.map_offdiag(sns.regplot,scatter=False, color="b")

