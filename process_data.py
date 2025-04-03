import numpy as np
from datetime import datetime
from fetch_data import fetch_bitcoin_data

def processed_data():
    raw_data = fetch_bitcoin_data()
    # Convert raw data into a list of (date, price) tuples
    cleaned_data = []
    for items in raw_data:
        date = items["date"]
        price = items["priceUsd"]
    # Ensure price is valid (not None or zero)
        if price and price != "null":
         date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
         cleaned_data.append((date, float(price)))

    # Sort by date
    cleaned_data.sort(key=lambda x: x[0])

    # Convert to NumPy array
    filtered_prices = np.array(cleaned_data, dtype=[("Date", "U10"), ("Price", "f4")])
    return filtered_prices

def calculate_metrix(prices):
    price_values = prices["Price"] 
    mean_price = np.mean(price_values)
    median_price = np.median(price_values)
    std_dev_price = np.std(price_values)

    # Print the metrics
    print("\nBitcoin Price Metrics:")
    print(f"Mean Price: ${mean_price:.2f}")
    print(f"Median Price: ${median_price:.2f}")
    print(f"Standard Deviation Price: ${std_dev_price:.2f}")

# Slicing the data
def slice_data(prices):
   print("First week data : ", prices[:7])
   print("Last week data : ", prices[-7:])

prices = processed_data()
calculate_metrix(prices)
slice_data(prices)