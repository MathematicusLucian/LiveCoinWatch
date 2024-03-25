import requests
from requests.adapters import HTTPAdapter
import json
import warnings

class LiveCoinWatch:

    def __init__(self, api_key=None, currency="GBP"):
        self.base_url = "https://api.livecoinwatch.com"
        self.currency = currency
        self.headers = {
            'content-type': 'application/json',
            'x-api-key': api_key if api_key!=None else "NO_API"
        }
        self.session = requests.Session()
        self.session.mount("https://", HTTPAdapter(max_retries=2))
        self.session.headers.update(self.headers)
        self.req_timeout = 120
    
    def __request(self, endpoint, payload):
        print(payload)
        url = "{}/{}".format(self.base_url, endpoint)
        print(url)
        try:
            res = self.session.post(url, data=json.dumps(payload), timeout=self.req_timeout)
            return json.loads(res.content.decode("utf-8"))
        except requests.exceptions.RequestException:
            raise

    def historic_values__coin(self, coin):
        endpoint = "coins/single/history"
        payload = {
            "code": coin,
            "currency": self.currency,
            "start": 1617035100000,
            "end": 1617035400000,
            "meta": True
        }
        return self.__request(endpoint, payload)

    def latest_values__coins(self, coins):
        endpoint = "coins/map"
        payload = {
            "codes": coins,
            "currency": self.currency,
            "sort": "rank",
            "order": "ascending",
            "offset": 0,
            "limit": 0,
            "meta": False
        }
        return self.__request(endpoint, payload)