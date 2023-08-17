import pybit
import os
import bybit

# Get the API key and secret from the environment variables
api_key = os.environ['BYBIT_API_KEY']
api_secret = os.environ['BYBIT_API_SECRET']

# Create a Bybit client object
client = bybit.bybit(test=False, api_key=api_key, api_secret=api_secret)

# Get the balance for each available coin
coins = ["BTC", "ETH", "EOS", "XRP", "USDT"]
for coin in coins:
    response = client.Wallet.Wallet_getBalance(coin=coin).result()[0]
    if 'result' in response:
        available_balance = response['result']['available_balance']
        if available_balance != 0:
            print(f"{coin} Balance: {available_balance:.8f} {coin}")
    else:
        print(f"{coin} balance not found.")