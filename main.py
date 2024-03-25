import requests
import json
from dotenv import dotenv_values

config = dotenv_values(".env")
LIVECOINWATCH_API_KEY = config['LIVECOINWATCH_API_KEY']
url = "https://api.livecoinwatch.com/coins/single"
payload = json.dumps({
  "currency": "USD",
  "code": "ETH",
  "meta": True
})
headers = {
  'content-type': 'application/json',
  'x-api-key': LIVECOINWATCH_API_KEY
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)