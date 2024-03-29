import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="Path to the file with prompt to send to the OpenAI API")
args = parser.parse_args()

# read file content
with open(args.file_path, 'r') as file:
    prompt = file.read()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

request_data = {
    "model": "text-davinci-003",
    "prompt": prompt,
    "max_tokens": 500,
    "temperature": 0.5,
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    print(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code)}")
