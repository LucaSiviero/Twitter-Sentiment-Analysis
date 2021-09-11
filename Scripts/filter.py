import re
import csv
import pandas as pd
"""
count = 0
csvImmuni = open('Immuni.csv', 'r')       #Accedo al file in modalità lettura
reader = csv.reader(csvImmuni)            #E lo preparo

for row in reader:                      #Scorro le righe
    count +=1
    print (row[1])                      #E stampo il secondo campo di ogni riga (il testo).

print (count)
"""

#Cancelliamo i duplicati all'interno del file Immuni.csv

#file_duplicates = "/home/luca/Scrivania/Progetto reti/Tweets/Immuni.csv"
file_duplicates = "/home/luca/Scrivania/Progetto reti/Tweets/ActualBadTweets.csv"
file_no_duplicates = "/home/luca/Scrivania/Progetto reti/Tweets/final.csv"
column_names = ['Testo']

df = pd.read_csv(file_duplicates, engine='python', sep = ",", names = column_names).drop_duplicates(['Testo'])

df.to_csv(file_no_duplicates, index = False)

print(df.head())

#Ok ha funzionato