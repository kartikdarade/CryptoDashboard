import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from process_data import processed_data
import numpy as np

def line_plot_btc_prices():
    data = processed_data()
    dates = data["Date"]
    prices = data["Price"]
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]
    plt.figure(figsize=(10, 5))
    plt.plot(dates, prices, linestyle='-', color='b', label="Bitcoin Price (USD)")

    # Formatting the chart
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title("Bitcoin Price Trend")

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  
    plt.xticks(rotation=45)  
    plt.legend()
    plt.grid()

    # Show the plot
    plt.show()

def bar_chart():
    data = processed_data()
    data = data[-7:]
    dates = data["Date"]
    prices = data["Price"]
    dates = [datetime.strptime(d,"%Y-%m-%d") for d in dates]
    plt.figure(figsize=(12,6))
    plt.bar(dates, prices, color = "Blue", label = "Bitcoin Prices")
    plt.xlabel("Date")
    plt.ylabel("Prices")
    plt.title("Bitcoin Price Trend for Last Week")
    plt.xticks(rotation = 45)

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))

    plt.legend()
    plt.grid(axis="y", linestyle = "--", alpha = 0.7)
    plt.show()


line_plot_btc_prices()