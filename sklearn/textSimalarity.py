#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:34:26 2016

@author: Varoon
"""

#This program takes 6 text files and compares how similar they are using a bag of words based on stems of those words.
#stems based on Natural Language Toolkit

from sklearn.feature_extraction.text import CountVectorizer
import nltk.stem
import scipy as sp
import sys
import os

stemmer = nltk.stem.SnowballStemmer('english')
class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: (stemmer.stem(w) for w in analyzer(doc))
vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')
#Stop words are words like "very" or "huge" that should not be weighted as importantly as other words


def dist_norm (v1,v2):
    
    return sp.linalg.norm((v1/sp.linalg.norm(v1.toarray())-v2/sp.linalg.norm(v2.toarray())).toarray())
    
best_doc=None
best_dist = sys.maxint
best_i=None
#name of directory with files to compare
DIR = "/Users/Varoon/Desktop/MachineLearningFiles/BuildingMachineLearningSystemsWithPython-master/ch03/data/toy"
posts = [open(os.path.join(DIR,f)).read() for f in os.listdir(DIR)]
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape
print ('#samples = %d, #features = %d' % (num_samples, num_features))
print vectorizer.get_feature_names()

test_post = "imaging database" #want to compare the text files to this string
test_post_vec = vectorizer.transform([test_post]) #array representation of instances of identified features
for i in range(0, num_samples):
    post = posts[i]
    if post==test_post:
        continue

    post_vec = X_train.getrow(i)

    d=dist_norm(post_vec, test_post_vec)
    print "--------> post %i with dist = %.2f: %s" % (i,d,post)
    
    if d<best_dist:
        best_dist = d
        best_i=i

print ("The best post is #%i with distance %.2f"%(best_i,best_dist))
