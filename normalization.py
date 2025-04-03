from process_data import processed_data
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime


def normalize_prices():
    data = processed_data()
    prices = data["Price"]

    min_price = np.min(prices)
    max_price = np.max(prices)

     # Print minimum and maximum price before normalization
    print(f"Minimum Price: {min_price:.2f} USD")
    print(f"Maximum Price: {max_price:.2f} USD")

    if max_price == min_price:
        return np.zeros_like(prices) 
    
    normalized_prices = (prices - min_price) / (max_price - min_price)
    return normalized_prices

def comparison_plot():
    data = processed_data()
    normalize_price = normalize_prices()
    regular_price = data["Price"]
    dates = [datetime.datetime.strptime(date_str, "%Y-%m-%d") for date_str in data["Date"]]

    # Plot both regular and normalized prices
    plt.figure(figsize=(12, 6))
    plt.plot(dates, regular_price, label="Regular Price (USD)", color="blue")
    plt.plot(dates, normalize_price * max(regular_price), label="Normalized Price (Scaled)", color="red", linestyle="dashed")

    # Improve readability
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title("Bitcoin Price vs. Normalized Price")

    # Format x-axis to show each month
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))  # Show each month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # Format as "Jan 2025"
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()



comparison_plot()