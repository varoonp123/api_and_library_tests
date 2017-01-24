#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 22:22:10 2016

@author: Varoon
"""

import tweepy

consumer_key='TpCYKB3NtWrkiRdVUUNmHx82h'
consumer_secret='jd5zqkdtjsu1uZHBUCwjBplTkrn3otYB7k54ljmDJ8VyQQoYXX'
access_token='791825707156594688-WDa6SKm0ihheIJKp5lKaISO30oLDPw7'
access_token_secret='cw09NaXRry3RdX0s3nssGp86y8ISr4gwKUoCYAHIdaIis'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api= tweepy.API(auth)


count =0
tweets = tweepy.Cursor(api.search,q="trump",geocode="40.7,-100.0,1000.0mi",count=5).items()
for tweet in tweets:
    print tweet.text
    
    
print tweets.num_tweets