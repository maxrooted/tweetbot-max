#!/usr/bin/python3

from retweets import *
from profile import *
from new_tweet import *
from tweetstream import *
import random
def Main():
    def My_twitter():
        me = api.me()
        myProfile = Myprofile(me.screen_name,me.followers_count,me.friends_count,me.id_str)
        myProfile._printProfile()
    def My_Tweet():
        newTweet = NewTweet("my_tweet.txt")
    def Stream_Tweet():
        myStreamListener = MyStreamListener()
        mystream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
        spesific_word = str(input("Set Hastag/Word #> "))
        mystream.filter(track=spesific_word.split())
    def _startretweet(data_id):
        with open(data_id,'r') as statuses_to_retweet:
            for x in statuses_to_retweet:
                api.retweet(x.rstrip())
                print ("success to retweet status with ID: {}".format(x.rstrip()))
                print ("Waiting...10 seconds")
                sleep(11)
    def Reply_Tweet():
        search_q = str(input("Set To Search #> "))
        messages = str(input("Set word in a status will u reply #> "))
        stwt = api.search(q=search_q, count=10)
        for stw in stwt:
            for message in messages.split():
                if message in stw.text:
                    tw_user = stw.user.screen_name
                    m = 'Happy Coding ! @{}'.format(tw_user)
                    s_reply = api.update_status(m, stw.id)
                    print ("Success Reply Tweet of @{}".format(tw_user))
                    sleep(60)
    while 1:
        print ("""
=====================================
TweetMX v1.0
+++++++++++++++++++++++++++++++++++++
Author : Mat Max
+++++++++++++++++++++++++++++++++++++
Author URL : http://www.maxrooted.com
+++++++++++++++++++++++++++++++++++++
[1] Show MyProfile
[2] Post New Tweet
[3] Grab Tweets and ID Tweets with Spesific Word
[4] Mass Retweets
[5] Auto reply Tweet
[0] Exit
""")
        menu = int(input("Choose Menu #> "))
        if menu == 1:
            My_twitter()
        elif menu == 2:
            My_Tweet()
        elif menu == 3:
            Stream_Tweet()
        elif menu == 4:
            _startretweet('status_id.txt')
        elif menu == 5:
            Reply_Tweet()
        elif menu == 0:
            exit()
Main()


