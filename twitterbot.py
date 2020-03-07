#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("/Users/alex/Documents/Coding_Projects/twitterbot/")
import tweepy, time
import random
from genesisList import genesis_sentences
from config import keys as k

def get_quote(sents):

    rand_index = random.randint(0,len(sents) - 1)
    curr_quote = sents[rand_index]# + sents[rand_index+1]

    return curr_quote + "\n Brought to you by Genesis_Bot : Praise Be!"

if __name__ == "__main__":
    get_quote(genesis_sentences)

auth = tweepy.OAuthHandler(k["CONSUMER_KEY"], k["CONSUMER_SECRET"])
auth.set_access_token(k["ACCESS_KEY"], k["ACCESS_SECRET"])
api = tweepy.API(auth)

while True:
    api.update_status(get_quote(genesis_sentences))
    time.sleep(43200) #Generates twice daily