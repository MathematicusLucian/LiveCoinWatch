import requests
from requests.adapters import HTTPAdapter
import json
import warnings
from dotenv import dotenv_values

config = dotenv_values(".env")
LIVECOINWATCH_API_KEY = config['LIVECOINWATCH_API_KEY']
CURRENCY = "GBP"
BASE_URL = "https://api.livecoinwatch.com/coins/"
HEADERS = {
  'content-type': 'application/json',
  'x-api-key': LIVECOINWATCH_API_KEY
}

def get_historic_values__coin(coin):
    return json.dumps({
        "code": coin,
        "currency": CURRENCY,
        "start": 1617035100000,
        "end": 1617035400000,
        "meta": True
    })

def latest_values__coins(coins):
    return json.dumps({
        "codes": coins,
        "currency": CURRENCY,
        "sort": "rank",
        "order": "ascending",
        "offset": 0,
        "limit": 0,
        "meta": False
    })

coins = ["ETH","BTC","XRP","SHIB"]

for coin in coins:
    payload__historic_values = get_historic_values__coin(coin)
    url = BASE_URL + "single/history"
    response = requests.request("POST", url, headers=HEADERS, data=payload__historic_values)
    print(response.text + "\n")
    
payload__latest_values = latest_values__coins(coins)
url = BASE_URL + "map"
response = requests.request("POST", url, headers=HEADERS, data=payload__latest_values)

print(response.text)