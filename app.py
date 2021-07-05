import pandas as pd
from pandas_datareader import data as web
import numpy as np
import matplotlib.pyplot as plt

# My Functions
from simulateStockChange import simulateStockChangeForAYear
from getStockInfo import getStockPrice, getStockPriceSeries


def investmentSimulator():

    # money = int(input("Enter your initial invesment:"))
    # ticker = input("Enter the symbol of the security you want to buy:")
    money = 5000
    ticker = "AAPL"
    currentStockPrice = getStockPrice(ticker)
    userShares = money/currentStockPrice
    state = True

    price_series = [currentStockPrice]

    while state:
        daily_return_percentages = simulateStockChangeForAYear(
            getStockPriceSeries(ticker))
        for i in daily_return_percentages:
            price_series.append(price_series[-1] * i)
        print("After " + str(int(len(price_series)/252)) + " year(s), the stock " +
              ticker + " closed at " + str(price_series[-1].round(2)) + ".")
        check = input(
            "Do you wish to continue the simulation? (Press n to end the simulation)")
        if check.lower() == "n":
            state = False

    plt.plot(price_series)
    plt.ylabel("Investment Value")
    plt.show()


investmentSimulator()
