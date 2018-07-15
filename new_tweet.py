#!/usr/bin/python3

from config import *

class NewTweet():

    def __init__(self,filename):
        self.filename = filename
        with open(self.filename,'r') as tweet:
            read_tweet = tweet.read()
            print ("[!] Starting Post Tweet: {}".format(read_tweet.rstrip()))
            if len(read_tweet) >= 257:
                print ("Character Has Limit !!!")
            else:
                api.update_status(read_tweet.rstrip())

