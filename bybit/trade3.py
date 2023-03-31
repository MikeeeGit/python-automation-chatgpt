import requests
import time
import hashlib
import hmac

# API Key and Secret
api_key = 'VkZ9VTuo8ksFnN5vI6'
api_secret = 'God8CMvev0IgEd9RIGNjPMeknca9THMyKExv'

# API Endpoint
url = "https://api.bybit.com/v2/private/wallet/balance"

# Request Headers
api_timestamp = str(int(time.time() * 1000))
api_signature = hmac.new(api_secret.encode(), f"GET/realtime{url}{api_timestamp}".encode(), hashlib.sha256).hexdigest()
headers = {
    "content-type": "application/json",
    "api_key": api_key,
    "api_signature": api_signature,
    "api_timestamp": api_timestamp
}

# Make the request
response = requests.get(url, headers=headers)

# Print the response
print(response.json())