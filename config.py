#!/usr/bin/python3

import tweepy
from time import sleep
""" Config File for Tweetbot """

consumer_key = 'YkuBtIWLICcuqvkQoqlz70Zst'
consumer_secret = 'JmyS7UNK2xxeUgmthSCPIUuFEfT44FV2VxvCmesT4upsD6beRz'
access_token = '978529541755777025-0dXKoAapCMPIOCg7wVbQMjvzMcEYqMN'
access_token_secret = 'H4Ah6KWJy5sZZ6SwbkupTORvdUJsQEOdtLniYL3IbUwIw'


# auth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Start to do twitterbot
api = tweepy.API(auth)
