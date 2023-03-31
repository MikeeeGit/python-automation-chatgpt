import requests
import time
import hashlib
import hmac
from urllib.parse import urlencode, urlparse

# API Key and Secret
api_key = 'VkZ9VTuo8ksFnN5vI6'
api_secret = 'God8CMvev0IgEd9RIGNjPMeknca9THMyKExv'

# API Endpoint
url = "https://api.bybit.com/v2/private/wallet/balance"

# Query Parameters
params = {
    "api_key": api_key,
    "api_timestamp": str(int(time.time() * 1000)),
}

# Sort query parameters alphabetically and encode them for the URL
encoded_params = urlencode(sorted(params.items()))

# Append the query parameters to the URL
parsed_url = urlparse(url)
signed_path = f"{parsed_url.path}?{encoded_params}"
signature = hmac.new(api_secret.encode(), signed_path.encode(), hashlib.sha256).hexdigest()
signed_url = f"{parsed_url.scheme}://{parsed_url.netloc}{signed_path}&api_signature={signature}"

# Make the request
response = requests.get(signed_url)

# Print the response
print(response.json())