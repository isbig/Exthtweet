#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import config
import os

#Twitter API credentials
consumer_key = config.a
consumer_secret = config.b
access_key = config.c
access_secret = config.d


def get_all_tweets(screen_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []  

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200, tweet_mode = 'extended')

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200 ,max_id=oldest, tweet_mode = 'extended')

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print ("...%s tweets downloaded so far" % (len(alltweets)))

    #transform the tweepy tweets into a 2D array that will populate the csv 
    outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text] for tweet in alltweets]

    dir_path = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(dir_path+"/result/csvfile"):
        os.makedirs(dir_path+"/result/csvfile")
    if not os.path.exists(dir_path+"/result/txtfile"):
        os.makedirs(dir_path+"/result/txtfile")
        
    #write the csv  
    with open(dir_path+"/result/csvfile/"+'%s_tweets.csv' % screen_name, 'w', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)

    with open(dir_path+"/result/txtfile/"+'%s_tweets.txt' % screen_name, 'w', encoding = 'utf-8') as f:
        for x in outtweets:
            f.write(x[2])

    pass


if __name__ == '__main__':
    # pass in the username of the account you want to download
    # ลิสต์ของ username
    m = []
    for a in m:
        print(a)
        get_all_tweets(a)
