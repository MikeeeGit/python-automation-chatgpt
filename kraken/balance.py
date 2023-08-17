###############
# Python Script to read from balance from Kraken
#
#
import os
import requests 
import json
import time
import urllib
import hmac
import base64
import hashlib


# Get the API key and secret from the environment variables
api_key = os.environ['KRAKEN_API_KEY']
api_secret = os.environ['KRAKEN_API_SECRET']

# Define the API endpoint and parameters
url = 'https://api.kraken.com/0/private/Balance'
nonce = str(int(time.time()*1000))
params = {'nonce': nonce}

# Create the API signature
postdata = urllib.parse.urlencode(params).encode('utf-8')
message = url.encode('utf-8') + hashlib.sha256(nonce.encode('utf-8') + postdata).digest()
signature = hmac.new(base64.b64decode(api_secret), message, hashlib.sha512)
sig_digest = base64.b64encode(signature.digest()).decode('utf-8')

# Add the signature to the request headers
headers = {
    'API-Key': api_key,
    'API-Sign': sig_digest
}

# Make the API request
response = requests.post(url, headers=headers, data=params)

# Check the response status code
if response.status_code != 200:
    print(f"Error: HTTP {response.status_code}")
    print(response.text)
    exit(1)

# Parse the response JSON
json_data = json.loads(response.text)

# Check if the JSON response has an 'error' key
if 'error' in json_data:
    print(f"Error: {json_data['error']}")
    exit(1)

# Display the balance for each currency
print("Total balance:")
for currency, balance in json_data['result'].items():
    print(f"{currency}: {balance}")
