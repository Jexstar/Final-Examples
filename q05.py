import yfinance as yf #pip install yfinance
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
from pandas import json_normalize
import requests
def q05():
    #Stock
    # https://saturncloud.io/blog/how-to-use-python-and-pandas-with-yahoo-finance-api/
    # Define the ticker list
    tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

    # Fetch the data
    data = yf.download(tickers_list, '2024-1-1')['Adj Close']

    # Plot all the close prices
    #colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan']  # Custom colors for each line
    #((data.pct_change() + 1).cumprod()).plot(figsize=(10, 7), color=colors)
    ((data.pct_change() + 1).cumprod()).plot(figsize=(10, 7))
    plt.legend()
    plt.title("Close Value", fontsize=16)

    # Define the labels
    plt.ylabel('Cumulative Close Value', fontsize=14)
    plt.xlabel('Time', fontsize=14)


    # Plot the grid lines
    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

    #plt.show()

    path = "C:\\Users\\ADMIN\\Desktop\\My Python Projects\\Final_Sheet01\\" + 'line05.png'
    plt.savefig(path)

