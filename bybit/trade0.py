# import requests
# import bybit
# import time
# import config

# client = bybit.bybit(test=False, api_key=config.api_key, api_secret=config.api_secret)

# print('loggedIn')

# # Make the API request
# response = client.Wallet.Wallet_getBalance(coin='BTC').result()

# # Print the response
# print(response[0]['result'][0]['available_balance'])


# import requests
# import json
# import config

# # API Endpoint
# url = "https://api.bybit.com/v5/account/balance"

# # Request Parameters
# params = {
#     "coin": "BTC",
#     "api_key": config.api_key,
#     "secret": config.api_secret
# }

# # Make the request
# response = requests.get(url, params=params)

# # Parse the response

# print(response.text)

# #data = json.loads(response.text)

# #print(response.txt)

# # Print the BTC balance
# #print("BTC Balance:", data['result']['BTC']['available'])




# import requests
# import json
# import config
# import time
# import hmac
# import hashlib

# # API Endpoint
# url = "https://api.bybit.com//v5/account/wallet-balance"

# # Request Parameters
# params = {
#     "coin": "BTC",
#     "api_key": config.api_key,
# }

# # Request Headers
# headers = {
#     "Content-Type": "application/json",
#     "api-signature-method": "HmacSHA256",
#     "api-key": config.api_key,
# }

# # Generate signature
# msg = f"{url}\n{json.dumps(params)}\n{int(time.time() * 1000)}\n"
# signature = hmac.new(config.api_secret.encode(), msg.encode(), hashlib.sha256).hexdigest()

# # Add signature to headers
# headers["api-signature"] = signature

# # Make the request
# response = requests.get(url, params=params, headers=headers)

# print(response.status_code) 

# # Print the response text
# print(response.text)

# # Parse the response
# data = json.loads(response.text)

# # Print the BTC balance
# print("BTC Balance:", data['result']['BTC']['available'])



import bybit
import config

# Create a Bybit client instance
client = bybit.bybit(test=False, api_key=config.api_key, api_secret=config.api_secret)

# Get wallet balance
balance = client.Wallet.Wallet_getBalance(coin="BTC").result()

print(balance[0])
print(balance[1])

# Print BTC balance
print(f"BTC Balance: {balance[0]['result']['BTC']['available_balance']}")


print ( {balance[0]['balance']})