import sys
import tweepy, time
import random
from genesisList import genesis_sentences
from config import keys as k

def get_quote(sents):

    rand_index = random.randint(0,len(sents) - 1)
    curr_quote = sents[rand_index]# + sents[rand_index+1]

    return curr_quote + "\nBrought to you by Genesis_Bot : Praise Be!"


auth = tweepy.OAuthHandler(k["CONSUMER_KEY"], k["CONSUMER_SECRET"])
auth.set_access_token(k["ACCESS_KEY"], k["ACCESS_SECRET"])
api = tweepy.API(auth)

while True:
    api.update_status(get_quote(genesis_sentences))
    time.sleep(43200) #Generates twice daily
