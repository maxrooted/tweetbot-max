#!/usr/bin/python3
from config import *
import random
_store_statuses_id = []
class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        print (status.text)
        print ("Status ID: {}".format(status.id_str))
        print ("Status ID Saved : {}".format(len(_store_statuses_id)))
        _store_statuses_id.append(status.id_str)
        if len(_store_statuses_id) < 10:
            with open('status_id.txt','w') as collect_id:
                collect_id.write('\n'.join(_store_statuses_id))
        else:
            exit()

