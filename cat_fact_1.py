import requests

# Replace with your actual API key
API_KEY = "your_api_key_here"

url = "https://api.thecatapi.com/v1/facts"

headers = {
    "x-api-key": API_KEY
}

params = {
    "limit": 1  # number of facts you want
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    for fact in data:
        print("🐱 Cat Fact:", fact["text"])
else:
    print("Error:", response.status_code, response.text)
