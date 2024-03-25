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

    def status(self):
        url = "status"
        payload = {}
        return self.__request(url, payload)

    def credits(self):
        url = "credits"
        payload = {}
        return self.__request(url, payload)

    def overview(self, **kwargs):
        url = "overview"
        payload = kwargs
        return self.__request(url, payload)

    def overview_history(self, **kwargs):
        endpoint = "overview/history"
        payload = { 
            "start": kwargs.get("start"),
            "end": kwargs.get("end")
        }
        return self.__request(endpoint, payload)

    def coin(self, **kwargs):
        endpoint = "coins/single"
        payload = { 
            "code": kwargs.get("code")
        }
        return self.__request(endpoint, payload)

    def coin__contract(self, **kwargs):
        endpoint = "coins/contract"
        payload = {
            "platform": kwargs.get("platform"),
            "address": kwargs.get("address")
        }
        return self.__request(endpoint, payload)

    def coin__history(self, **kwargs):
        endpoint = "coins/single/history"
        payload = {
            "code": kwargs.get("code"),
            "currency": kwargs.get("currency"),
            "start": kwargs.get("start"),
            "end": kwargs.get("end"),
            "meta": True
        }
        return self.__request(endpoint, payload)

    def coins__list(self, **kwargs):
        endpoint = "coins/list"
        payload = kwargs
        return self.__request(endpoint, payload)

    def coins__map(self, **kwargs):
        endpoint = "coins/map"
        payload = {
            "codes": kwargs.get("codes"),
            "currency": kwargs.get("currency"),
            "sort": kwargs.get("sort"),
            "order": "ascending",
            "offset": kwargs.get("offset"),
            "limit": kwargs.get("limit"),
            "meta": False
        }
        return self.__request(endpoint, payload)

    def fiats(self):
        endpoint = "fiats/all"
        payload = {}
        return self.__request(endpoint, payload)

    def exchanges_single(self, **kwargs):
        endpoint = "exchanges/single"
        payload = {
            "code": kwargs.get("code")
        }
        return self.__request(endpoint, payload)

    def exchanges_list(self, **kwargs):
        endpoint = "exchanges/list"
        payload = kwargs
        return self.__request(endpoint, payload)
    
    def platforms_all(self):
        endpoint = "platforms/all"
        payload = {}
        return self.__request(endpoint, payload)