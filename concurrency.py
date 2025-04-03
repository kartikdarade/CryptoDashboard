import requests
import threading
import time

cryptos = ["bitcoin", "solana", "cardano", "ethereum"]

def fetch_crypto_data(crypto, retries=5, delay=3):
    """Fetch historical price data for a given cryptocurrency with retries."""
    url = f"https://api.coincap.io/v2/assets/{crypto}/history?interval=d1"

    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                
                if "data" in data and data["data"]:
                    latest_price = float(data["data"][-1]["priceUsd"])  # Convert to float
                    print(f"✅ {crypto.capitalize()} data fetched successfully!")
                    print(f"🔹 {crypto.capitalize()} latest price: ${latest_price:.2f}\n")
                else:
                    print(f"⚠️ No price data found for {crypto}.")

                return  # Exit after successful fetch

            elif response.status_code == 429:
                print(f"🚨 Rate limit hit for {crypto}. Retrying in {delay} seconds... (Attempt {attempt+1})")
                time.sleep(delay)  # Wait before retrying

            else:
                print(f"❌ Failed to fetch data for {crypto} (Status Code: {response.status_code})")
                return  # Exit if other errors occur

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Network error for {crypto}: {e}")

    print(f"❌ Giving up on {crypto} after {retries} attempts.")

# Create and start threads for each cryptocurrency
threads = []
for crypto in cryptos:
    thread = threading.Thread(target=fetch_crypto_data, args=(crypto,))
    threads.append(thread)
    thread.start()
    time.sleep(1)  # Small delay to reduce API load

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("🚀 All cryptocurrency data fetched!")
