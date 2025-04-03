import requests
import threading
import time
import matplotlib.pyplot as plt

# List of cryptocurrencies to track
cryptos = ["bitcoin", "solana", "cardano", "ethereum"]
crypto_prices = {}  # Dictionary to store real-time prices

# Interval in seconds for updating the chart
UPDATE_INTERVAL = 5  

def fetch_crypto_data():
    """Fetch latest cryptocurrency prices and update global dictionary."""
    for crypto in cryptos:
        url = f"https://api.coincap.io/v2/assets/{crypto}/history?interval=d1"
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if "data" in data and data["data"]:
                    latest_price = float(data["data"][-1]["priceUsd"])
                    crypto_prices[crypto.capitalize()] = latest_price
                    print(f"✅ {crypto.capitalize()} updated price: ${latest_price:.2f}")
                else:
                    print(f"⚠️ No data for {crypto}.")
            elif response.status_code == 429:
                print(f"🚨 Rate limit hit for {crypto}, skipping this update.")

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Network error for {crypto}: {e}")

    # Schedule the next update
    threading.Timer(UPDATE_INTERVAL, fetch_crypto_data).start()

def plot_crypto_prices():
    """Continuously update and display the bar chart in real-time."""
    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots(figsize=(8, 5))

    while True:
        ax.clear()  # Clear the previous plot
        if not crypto_prices:
            print("❌ No data available for plotting.")
            time.sleep(UPDATE_INTERVAL)
            continue
        
        ax.bar(crypto_prices.keys(), crypto_prices.values(), color=["blue", "orange", "green"])
        
        ax.set_xlabel("Cryptocurrency")
        ax.set_ylabel("Price in USD")
        ax.set_title("Real-Time Cryptocurrency Prices")
        ax.set_xticks(range(len(crypto_prices)))
        ax.set_xticklabels(crypto_prices.keys(), rotation=30)
        ax.grid(axis="y", linestyle="--", alpha=0.7)

        # Annotate bars with prices
        for i, (crypto, price) in enumerate(crypto_prices.items()):
            ax.text(i, price + (price * 0.02), f"${price}", ha="center", fontsize=10, fontweight="bold")

        plt.draw()
        plt.pause(UPDATE_INTERVAL)  # Pause to allow real-time updates

# Start fetching real-time prices
fetch_crypto_data()

# Start the real-time chart update
plot_crypto_prices()
