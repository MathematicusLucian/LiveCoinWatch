# LiveCoinWatch

A Python interface for the (LiveCoinWatch API)[https://www.livecoinwatch.com/]

## Install

```bash
pip install LiveCoinWatch
```

## Env
Create: ``python3source myvenv/bin/activate -m venv venv``

Active: ``source venv/bin/activate``

## Implementation

```python
from livecoinwatch import LiveCoinWatch
coin_data = LiveCoinWatch("<YOUR_API_KEY>")
```

## Example

```python
from livecoinwatch import LiveCoinWatch
from dotenv import dotenv_values

config = dotenv_values(".env")
api_key = config['LIVECOINWATCH_API_KEY']
base_currency = "GBP"
coins = ["ETH","BTC","XRP","SHIB"]
coin_data = LiveCoinWatch(api_key, "GBP")

for coin in coins:
    # Call 'coins/single/history'
    historic_values = coin_data.coin__history(
        code=coin,
        currency=base_currency,
        start=1617035100000,
        end=1617035400000)
    print(historic_values)
    print("\n")

# Call 'coins/map'
latest_values = coin_data.coins__map(
            codes= coins,
            currency=base_currency,
            sort="rank",
            offset=0,
            limit=0)
print(latest_values)
```
