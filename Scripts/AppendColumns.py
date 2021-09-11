import pandas as pd
import csv
import re

filepath = "/home/luca/Scrivania/Progetto reti/Tweets/BadTweets.csv"
file2 = "/home/luca/Scrivania/Progetto reti/Tweets/final.csv"
csvWriter = open(file2, "w")

with open(filepath, "r") as csvFile:
    for row in csvFile:
        stringa = re.sub('[,][\n][,]+', ',', row)
        csvWriter.write(stringa)