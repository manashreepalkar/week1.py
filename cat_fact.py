import requests

API_URL = "https://catfact.ninja/fact"

def get_cat_fact():
    try:
        # Make request with timeout
        response = requests.get(API_URL, timeout=5)

        # Raise error for bad HTTP status
        response.raise_for_status()

        # Parse JSON
        data = response.json()

        # Print at least 3 fields
        print("Cat Fact:", data.get("fact"))
        print("Fact Length:", data.get("length"))
        print("HTTP Status Code:", response.status_code)

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Check your internet connection.")

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection or API unreachable.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")

    except ValueError:
        print("Error: Failed to parse JSON response.")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    get_cat_fact()
