import requests
import pandas as pd
import time
import json

# Loading data from 6 November 2021 to Wed 1 December 2021
def data_history():
    url = 'https://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start=1636156800000&end=1638316800000'

    payload = {}
    headers= {}

    response = requests.request('GET', url, headers = headers, data = payload)

    json_data = json.loads(response.text.encode('utf-8-sig'))
    bitcoin_data = json_data['data']
    df = pd.DataFrame(bitcoin_data)
    df.to_csv('bitcoin-usd.csv', index = False)

# data_history()

def data_new():
    timestamp = int(time.time()*1000.0) #Time at the moment
    end_timestamp = pd.read_csv('bitcoin-usd.csv').iloc[-1]['time'] # Time in the last line of the csv file

    url = f'https://api.coincap.io/v2/assets/bitcoin/history?interval=d1&start={int(end_timestamp) + 86400000}&end={timestamp}'

    payload = {}
    headers= {}

    response = requests.request('GET', url, headers = headers, data = payload)

    json_data = json.loads(response.text.encode('utf-8-sig'))
    bitcoin_data = json_data['data']
    df = pd.DataFrame(bitcoin_data)
    df.to_csv('bitcoin-usd.csv', mode = 'a', header = False, index = False)

data_new()
