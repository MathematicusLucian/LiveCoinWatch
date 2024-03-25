# LiveCoinWatch

***This package is available at: [pypi.org/project/LiveCoinWatch/1.0.0/](pypi.org/project/LiveCoinWatch/1.0.0/)***

A Python interface for the [LiveCoinWatch API](https://www.livecoinwatch.com/)

## Install

```bash
pip install LiveCoinWatch==1.0.0
```

## Env
Create: ``python3 -m venv venv``

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

## Uploading to PyPi
Used Twine: ```python3 -m pip install --upgrade build```

```python3 -m pip install --upgrade twine```

Build: ```python3 -m build```

Upload to PyPi: ```python3 -m twine upload dist/*```

Upload to TestPyPi: ```python3 -m twine upload --repository testpypi dist/*```

(.pypirc in $HOME directory)

View at: ```https://test.pypi.org/project/LiveCoinWatch/1.0.0/```

Install: ``pip install LiveCoinWatch==1.0.0``

Install (TestPyPi): ``python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps LiveCoinWatch``