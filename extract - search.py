#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import os
import config

#Variables that contains the user credentials to access Twitter API 
access_token = config.c
access_token_secret = config.d
consumer_key = config.a
consumer_secret = config.b

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

dir_path = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(dir_path+"/result/searchtwit"):
    os.makedirs(dir_path+"/result/searchtwit")

#modified code from https://www.quora.com/How-do-you-do-a-search-on-Twitter-that-filters-out-duplicate-tweets-(Or-at-least-retweets-)
def hatweet(kamtiha, chamnuan):
    with open(dir_path+"/result/searchtwit/"+'%s_twit.txt' %kamtiha, 'w', encoding = 'utf-8') as f:
        for status in tweepy.Cursor(api.search,q=kamtiha+" -filter:retweets",lang='th', tweet_mode = 'extended', result_type='recent').items(chamnuan):
            f.write(status.full_text+"\n")

hatweet("บุพเพสันนิวาส", 300)
