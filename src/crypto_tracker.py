import requests
from requests.adapters import HTTPAdapter
import json
import warnings

class CryptoTracker:

    def __init__(self, api_key=None, currency="GBP"):
        self.base_url = "https://api.livecoinwatch.com"
        self.currency = currency
        self.headers = {
        'content-type': 'application/json',
        'x-api-key': api_key 
        }

    def get_historic_values__coin(self, coin):
        return json.dumps({
            "code": coin,
            "currency": self.currency,
            "start": 1617035100000,
            "end": 1617035400000,
            "meta": True
        })

    def latest_values__coins(self, coins):
        return json.dumps({
            "codes": coins,
            "currency": self.currency,
            "sort": "rank",
            "order": "ascending",
            "offset": 0,
            "limit": 0,
            "meta": False
        })
    
    def fetch_coin_data(self, url, payload):
        url = self.base_url + url
        return requests.request("POST", url, headers=self.headers, data=payload)