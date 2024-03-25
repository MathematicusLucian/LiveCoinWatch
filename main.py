from src.crypto_tracker import CryptoTracker
from dotenv import dotenv_values
config = dotenv_values(".env")

coins = ["ETH","BTC","XRP","SHIB"]
tracker = CryptoTracker(config['LIVECOINWATCH_API_KEY'], "GBP")

for coin in coins:
    payload__historic_values = tracker.get_historic_values__coin(coin)
    url = "/coins/single/history"
    response = tracker.fetch_coin_data(url, payload__historic_values)
    print(response.text + "\n")
    
payload__latest_values = tracker.latest_values__coins(coins)
url = "/coins/map"
tracker.fetch_coin_data(url, payload__latest_values)
print(response.text)