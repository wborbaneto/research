# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 20:37:37 2018

@author: AHCI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import algorithm as alg
#'Consumo','RPM','MAF','Velocidade','Aceleracao','CargaMotor'
cl3 = pd.read_csv('data/agressiva.csv')
cl2 = pd.read_csv('data/normal.csv')
cl1 = pd.read_csv('data/lenta.csv')

irisdf = pd.read_csv('data/iris.csv')
iris = np.array(irisdf.values[:,0:4],dtype='float64')

a,b,c = cl1.shape[0],cl2.shape[0],cl3.shape[0]
r = [a,b,c]
r = np.min(r)

a,b,c = 50,50,50
cl1 = iris[0:a,:]
cl2 = iris[a:a+b,:]
cl3 = iris[a+b:a+b+c,:]

#cl3 = np.array(cl3.values)
#cl2 = np.array(cl2.values)
#cl1 = np.array(cl1.values)

x = np.r_[cl1,cl2,cl3]
y = alg.outputb(3,[a,b,c])

x =  (x - np.min(x,0))/(np.max(x,0) - np.min(x,0))

xx = x.T
S = np.cov(xx)
S = np.linalg.inv(S)
x1 = x[40,:]
#a = np.array([[64,66,68,69,73],[580,570,590,660,600],[29,33,37,46,55]])
#mi = np.mean(a,1)
#S = np.cov(a)
#S = np.linalg.inv(S)
#x = np.array([66,640,44])
A = x1[None].T - x.T
A2 = x1[None].T - x[0,:][None].T
dist = np.diag(np.sqrt(abs(A.T@S@A)))
dist2 = np.sqrt(abs(A2.T@S@A2))