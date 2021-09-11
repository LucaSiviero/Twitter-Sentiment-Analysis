import csv

tweets_path = "/home/luca/Scrivania/Progetto reti/Tweets/Tweets.csv"
immuni_path = "/home/luca/Scrivania/Progetto reti/Tweets/Immuni.csv"
badTweets = "/home/luca/Scrivania/Progetto reti/Tweets/final.csv"

tweet_count = 0
with open(tweets_path, "r") as tweetsFile:
    for row in tweetsFile:
        tweet_count += 1

print("Il numero totale di tweets ottenuto attraverso la twitter API è: " + str(tweet_count))

immuni_count = 0
with open(immuni_path, "r") as immuniFile:
    for row in immuniFile:
        immuni_count += 1

discussion_rate = (immuni_count / tweet_count) * 100

print("Il rapporto di discussione della tematica immuni sui tweets ottenuti è del " + str(discussion_rate) + "%" + ". I tweet su Immuni sono: " + str(immuni_count))

bad_tweet_count = 0

with open(badTweets, 'r') as badFile:
    for row in badFile:
        bad_tweet_count += 1

bad_rate = (bad_tweet_count/20374) * 100
print("Si parla male di Immuni nel " + str(bad_rate) + "% dei casi" + ". I tweet che parlano male di immuni sono: " + str(bad_tweet_count)) 

#Lo script evince che la tematica Immuni è trattata nel 27.7% dei casi rispetto alle tematiche generali.