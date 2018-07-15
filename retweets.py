#!/usr/bin/python3

from config import *

def _startretweet(data_id):
    with open(data_id,'r') as statuses_to_retweet:
        for x in statuses_to_retweet:
            api.retweet(x.rstrip())
            print ("success to retweet status with ID: {}".format(x.rstrip()))
            print ("Waiting...10 seconds")
            sleep(11)
