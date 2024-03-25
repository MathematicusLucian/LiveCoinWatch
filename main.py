from src.livecoinwatch import LiveCoinWatch
from dotenv import dotenv_values

config = dotenv_values(".env")
base_currency = "GBP"
coins = ["ETH","BTC","XRP","SHIB"]

coin_data = LiveCoinWatch(config['LIVECOINWATCH_API_KEY'], "GBP")
for coin in coins:
    historic_values = coin_data.coin__history(
        code=coin,
        currency=base_currency,
        start=1617035100000,
        end=1617035400000)
    print(historic_values)
    print("\n")
    
latest_values = coin_data.coins__map(
            codes= coins,
            currency=base_currency,
            sort="rank",
            offset=0,
            limit=0)
print(latest_values)