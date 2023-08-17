import bybit
import pybit
import os


# Get the API key and secret from the environment variables
api_key = os.environ['BYBIT_API_KEY']
api_secret = os.environ['BYBIT_API_SECRET']

# Create a Bybit client object
client = bybit.bybit(test=False, api_key=api_key, api_secret=api_secret)

# Get the BTC balance
response = client.Wallet.Wallet_getBalance(coin='BTC').result()[0]

# Print the BTC balance
if 'result' in response:
    btc_balance = response['result']['BTC']['available_balance']
    print(f"BTC Balance: {btc_balance:.8f} BTC")
else:
    print("BTC balance not found.")