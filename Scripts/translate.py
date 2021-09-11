# -*- coding: utf-8 -*-

# This simple app uses the '/translate' resource to translate text from
# one language to another.

import os, requests, uuid, json
import csv
import pandas as pd

subscription_key = ''       #Subscription key per il translator


endpoint = 'https://api.cognitive.microsofttranslator.com/'     #Endpoint della connessione
position = 'westeurope'


path = '/translate?api-version=3.0'
params = '&from=it&to=en'
constructed_url = endpoint + path + params          #URL di connessione

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,      #Passiamo la key e la regione
    'Ocp-Apim-Subscription-Region': position,
    'Content-type': 'application/json',                 #Specificando che vogliamo avere indietro un JSON.
    'X-ClientTraceId': str(uuid.uuid4())
}

file_it = '/home/luca/Scrivania/Progetto reti/Cleaned Tweets/Immuni_no_duplicates.csv'
file_en = '/home/luca/Scrivania/Progetto reti/Translated Tweets/Immuni_translated.csv'
column_names = ['Data','Testo','Optional']

df = pd.read_csv(file_it, engine='python', sep = ",", names = column_names)
Writer = open(file_en, "a")
csvWriter = csv.writer(Writer)
#Nel body possiamo passare più di un oggetto ma in realtà in questo caso dobbiamo iterare le righe dell'excel e tradurre il tutto.   


for row in df['Testo']:
    body = [{
        'text' : row
    }]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    csvWriter.writerow(response[0]["translations"][0]["text"])
    

#print(response[0]["translations"][0]["text"])