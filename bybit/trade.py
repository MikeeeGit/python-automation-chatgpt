# Bybit API key name:bybitapi
# Bybit API Key: VkZ9VTuo8ksFnN5vI6
# Bybit API Secret: God8CMvev0IgEd9RIGNjPMeknca9THMyKExv

import requests

# API Key and Secret
api_key = 'VkZ9VTuo8ksFnN5vI6'
api_secret = 'God8CMvev0IgEd9RIGNjPMeknca9THMyKExv'

# API Endpoint
url = "https://api.bybit.com/v2/private/wallet/balance"

# Request Headers
headers = {
    "Content-Type": "application/json",
    "X-API-KEY": api_key,
    "X-API-SECRET": api_secret
}

# Make the request
response = requests.get(url, headers=headers)

# Print the response
print(response.json())