import os
import tweepy
from tweepy import OAuthHandler

"""
This is the authentication items that are going to be needed in order to access the twitter API

We are going to use the OAuth interface

We could import the entire tweepy library and if we do that then we need to specify what we need want to use

"""

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


# this is now the entry point for the authentication application - this is how we can interact with twitter/x
api = tweepy.API(auth)


# Creating a function to process or store 

