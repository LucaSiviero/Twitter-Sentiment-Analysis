import tweepy
import csv
import pandas as pd
####Credenziali
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
# File da scrivere
csvFile = open('/home/luca/Scrivania/Progetto reti/Tweets/Immuni.csv', 'a')
#Si usa csv.writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q = "#Immuni", count=100,
                           lang="it",
                           since="2020-12-01").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text])
