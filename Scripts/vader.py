from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer    #Importo il sentiment analyzer
import csv

#Gli score compund più alti di 0.5 sono positivi.

analyzer = SentimentIntensityAnalyzer()

file_to_analyze = "/home/luca/Scrivania/Progetto reti/Translated Tweets/Definitive_translation.csv"
reader = open(file_to_analyze, "r")
csvReader = csv.reader(reader)
file_to_write = "/home/luca/Scrivania/Progetto reti/Tweets/BadTweets.csv"
writer = open(file_to_write, "a")
csvWriter = csv.writer(writer)

for row in csvReader:
    sentence = row[0]
    score = analyzer.polarity_scores(sentence)
    if score['neg'] >= 0.3 or (score['neu'] <= 0.5 and score['pos'] <= 0):
        csvWriter.writerow(sentence)

#print(score['compound'])
#print("{:-<40} {}".format(sentence, score))


