"""

This class takes in the StreamListener and listens to a certain keyword and then stores is in a dictionary of json responses to be accessed later

The inputs that this will need is the streamer and the keyword that is going to be listened to and then amount of tweets to get

"""

import tweepy
from tweepy import StreamListener

class PythonStreamer:
    def __init__(self, api, keyword, tweet_count, stream_listener):

        # These are created on initlization and need to be passed in
        self.stream_listener = stream_listener
        self.api = api
        self.keyword = keyword
        self.tweet_count = tweet_count

        # this is a disctionary that will hold the tweets that are going to be collected
        self.tweets = {}

        #TODO

        # listend to events and then process them we will need to handle the data and if it is a bad response handle that as well
