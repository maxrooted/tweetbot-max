#!/usr/bin/python3

from config import *


class Myprofile:

    def __init__(self,username,follower,following,myid):
        self.username = username
        self.follower = follower
        self.following = following
        self.myid = myid
    def _printProfile(self):
        print (" MYPROFILE ".center(20,"+"))
        print ("Username : {}".format(self.username))
        print ("Follower : {}".format(self.follower))
        print ("Following : {}".format(self.following))
        print ("My ID : {}".format(self.myid))
        print ("".center(20,"+"))

