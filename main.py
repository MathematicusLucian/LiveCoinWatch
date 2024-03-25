from src.livecoinwatch import LiveCoinWatch
from dotenv import dotenv_values
config = dotenv_values(".env")

coins = ["ETH","BTC","XRP","SHIB"]
tracker = LiveCoinWatch(config['LIVECOINWATCH_API_KEY'], "GBP")

for coin in coins:
    historic_values = tracker.historic_values__coin(coin)
    print(historic_values)
    print("\n")
    
latest_values = tracker.latest_values__coins(coins)
print(latest_values)