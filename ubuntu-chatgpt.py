import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
#    "model": "gpt-4-32k-0613",
     "model": "text-davinci-003",
#    "model": "gpt-3.5-turbo",
    "prompt": f"In Ubuntu 22.04.3 LTS provide commands or script {args.prompt}. Provide only code, no text",
#    "prompt": f"{args.prompt}",
    "max_tokens": 800,
    "temperature": 0.5,
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    print(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code)}")