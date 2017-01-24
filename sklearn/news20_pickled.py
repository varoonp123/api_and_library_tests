#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:26:02 2016

@author: Varoon
"""
from clustering_news20 import StemmedTfidfVectorizer
from sklearn.externals import joblib
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk.stem
import scipy as sp

#TFID vectorizer weights words in every doc less (like 'a' or 'but'). Ignore words that appear fewer than 5 times or more than 1/2 of the time in a doc.
#stop words as previously defined. Ignore unknown chars
vectorizer = StemmedTfidfVectorizer(min_df=10, max_df=.5, stop_words='english', decode_error='ignore')
vectorized = joblib.load('vectorized_news_20.pkl')
print 'vec loaded'
num_samples, num_features = vectorized.shape

km = joblib.load('news20Fit.pkl')
print 'km loaded'

new_post = "Disk drive problems. Hi, I have a problem with my hard disk. After 1 year it is working only sporadically now. I tried to format it, but now it doesn't boot any more. Any ideas? Thanks."
new_post_vec = vectorizer.transform([new_post])


new_post_label = km.predict(new_post_vec)[0]
similar_indices = (km.labels_==new_post_label).nonzero()[0]     #get indices of posts in same cluster
similar=[]

for i in similar_indices:
    dist = sp.linalg.norm((new_post_vec - vectorized[i]).toarray())
    similar.append((dist,dataset.data[i]))
    
similar=sorted(similar)

#dump the trained model into a pickled version to avoid retraining
joblib.dump(km, 'news20Fit.pkl')
print similar[0]
print similar[len(similar)-1]