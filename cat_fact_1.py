import requests

def get_cat_fact(api_key):
    # API Ninjas endpoint for facts
    # You can append '?limit=3' to the URL to get more than one fact
    url = 'https://api.api-ninjas.com/v1/facts?limit=1'
    
    # The API key must be passed in the 'X-Api-Key' header
    headers = {'X-Api-Key': api_key}
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # The API returns a list of dictionaries
            fact = data[0]['fact']
            return fact
        else:
            return f"Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"An error occurred: {e}"

# --- Execution ---
MY_API_KEY = 'YOUR_ACTUAL_API_KEY_HERE'
fact = get_cat_fact(MY_API_KEY)

print(f"🐱 Cat Fact: {fact}")
