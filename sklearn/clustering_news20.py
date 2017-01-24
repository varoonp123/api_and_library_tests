 #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 23:01:06 2016

@author: Varoon
"""

"""
Exercise to cluster dataset from 20 newsgroups. Then check results against new post. 

"""

import sklearn.datasets
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk.stem
from sklearn.cluster import KMeans
from sklearn.externals import joblib

import scipy as sp
#tfidf= term freq-inverse document frequency. Higher val if in doc many times. Lower freq if in many docs

english_stemmer = nltk.stem.SnowballStemmer('english')
class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))
DIR = "/Users/Varoon/Desktop/MachineLearningFiles/BuildingMachineLearningSystemsWithPython-master/"
dataset = sklearn.datasets.load_mlcomp("20news-18828", mlcomp_root = DIR)

print (dataset.filenames)



#only take some groups for simplicity
groups = ['comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.ma c.hardware', 'comp.windows.x', 'sci.space']

test_data = sklearn.datasets.load_mlcomp("20news-18828", "test",mlcomp_root = DIR, categories=groups)
train_data = sklearn.datasets.load_mlcomp("20news-18828", "train",mlcomp_root = DIR, categories=groups)
print ("There are %i training files and %i test files."%(len(train_data.filenames), len(test_data.filenames)))

#TFID vectorizer weights words in every doc less (like 'a' or 'but'). Ignore words that appear fewer than 5 times or more than 1/2 of the time in a doc.
#stop words as previously defined. Ignore unknown chars
 
gvectorizer = StemmedTfidfVectorizer(min_df=10, max_df=.5, stop_words='english', decode_error='ignore')
vectorized = vectorizer.fit_transform(dataset.data)

joblib.dump(vectorized, 'vectorized_news_20.pkl')
num_samples, num_features = vectorized.shape
print('There are %i samples and %i features.' %(num_samples, num_features))
"""
num_clusters = 50
#initialize kmeans clustering
km = KMeans(n_clusters=num_clusters, init='random',n_init=1,verbose=1)
km.fit(vectorized)


#want to cluster the following post:
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
"""