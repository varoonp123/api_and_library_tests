#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:00:19 2016

@author: Varoon
"""
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
#import numpy as np

#load iris dataset from sklearn
data=load_iris()
features=data['data']
feature_names = data['feature_names']
target=data['target']

for t,marker,c in zip(xrange(3), ">ox", "rgb"):
    plt.scatter(features[target==t,0],features[target==t,1],
                marker=marker,c=c)
    
