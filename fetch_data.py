import requests
import time

def fetch_bitcoin_data(retries=5, delay=3):
    url = "https://api.coincap.io/v2/assets/bitcoin/history?interval=d1"

    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)  # Timeout added
            if response.status_code == 200:
                data = response.json()
                print("✅ Data fetched successfully!")
                return data["data"]
            else:
                print(f"❌ Attempt {attempt+1}: Failed to fetch data (Status Code: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Attempt {attempt+1}: Network error - {e}")

        if attempt < retries - 1:
            print(f"🔄 Retrying in {delay} seconds...")
            time.sleep(delay)

    raise Exception("🚨 Failed to fetch Bitcoin data after multiple attempts. API may be down.")
