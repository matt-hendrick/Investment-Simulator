import pandas as pd
from pandas_datareader import data as web
import numpy as np
import matplotlib.pyplot as plt

# My Functions
from calculateStockChange import calculateStockChangeForAYear
from getStockInfo import getStockPrice, getStockPriceSeries


def runSimulation(initialInvestment=10000, ticker="AAPL"):

    initialInvestment = int(initialInvestment)

    currentStockPrice = getStockPrice(ticker)
    userShares = initialInvestment/currentStockPrice
    state = True

    price_series = [currentStockPrice]

    while state:
        daily_return_percentages = calculateStockChangeForAYear(
            getStockPriceSeries(ticker))
        for i in daily_return_percentages:
            price_series.append(price_series[-1] * i)
        print("After " + str(int(len(price_series)/21)) + " month(s), the stock " +
              ticker + " closed at " + str(price_series[-1].round(2)) + ".")
        check = input(
            "Do you wish to continue the simulation? (Press n to end the simulation)")
        if check.lower() == "n":
            state = False

    percent_change = (price_series[-1] -
                      currentStockPrice) / currentStockPrice * 100
    plt.plot(price_series)
    plt.ylabel("Investment Value")
    plt.show()
