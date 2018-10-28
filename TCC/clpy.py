# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 21:19:17 2018

@author: AHCI
"""
import numpy as np


def outputb(numC, slices):
    y = np.zeros([1,numC])
    for s in range(0,numC):
        buffer = np.zeros([1, numC])
        buffer[:,s] = 1
        y = np.r_[ y,np.tile(buffer,(slices[s],1))]
    return y[1:,:]

def outputd(numC, slices):
    y = np.zeros([1,1])
    for s in range(0,numC):
        y = np.r_[ y,np.tile(s,(slices[s],1))]
    return y[1:,:]

def outputs(numC, slices, names):
    y = np.zeros([1,1])
    for s in range(0,numC):
        y = np.r_[ y,np.tile(names[s],(slices[s],1))]
    return y[1:,:]

def dec2str(winners, names):
    numC = len(names)
    y = np.tile("               ",(winners.shape))
    for s in range(0,numC):
        y[(winners==s).ravel()] = names[s]
    return y

def bin2str(binary, names):
    numC = len(names)
    y = np.tile("               ",(binary.shape[0],1))
    for s in range(0,numC):
        buffer = np.zeros([1, numC])
        buffer[:,s] = 1
        y[np.all(binary==buffer,1).ravel()] = names[s]
    return y