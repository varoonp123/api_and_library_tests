#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:06:54 2016

@author: Varoon
"""

#shows how iris petal length good for distinguishing 

#from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
import os

#CountVectorizer is "bag of words" method. Counting number of distinct words in a string
vectorizer=CountVectorizer(min_df=1)

#min_df (min document frequency) describes what to do with rare words. 
#min_df=n drops words with fewer with n occurrences 
# /drops words appearing with freq less than n when  n is a frac

content=["How to format my hard disk", " Hard disk format problems "]

X = vectorizer.fit_transform(content)

print vectorizer.get_feature_names()

print X.toarray().transpose()
#this len(content)xlen(vectorizer.get_geature_names()) prints the num times each 
#feature name appears in each sentence in content

#folder contains 4 text files with various sentences
file_path = '/Users/Varoon/Desktop/MachineLearningFiles/BuildingMachineLearningSystemsWithPython-master/ch03/data/toy'
posts = [open(os.path.join(file_path,f)).read() for f in os.listdir(file_path)]
vectorizer2=CountVectorizer(min_df=1)

X_train=vectorizer2.fit_transform(posts)
num_samples, num_features=X_train.shape

print("#samples: %d, #features: %d" % (num_samples,
        num_features)) #samples: 5, #features: 25

def norm                                       