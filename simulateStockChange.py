import math
import numpy as np


def simulateStockChangeForAYear(price_series):

    total_growth = price_series['Close'][-1] / price_series['Close'][0]

    # determines years elapsed by calculating size of price_series DF and dividing by trading days
    # there are 252 trading days in the year
    years_elapsed = (len(price_series))/252
    annualized_growth_rate = total_growth / years_elapsed

    # gets standard deviation of closing price_series
    std = price_series["Close"].pct_change().std()
    std = std * math.sqrt(252)

    return np.random.normal(
        (annualized_growth_rate/252), std/math.sqrt(252), 252)+1

    # price_series = [price_series['Close'][0]]

    # for i in daily_return_percentages:
    #     price_series.append(price_series[-1] * i)

    # plt.plot(price_series)
    # plt.show()

    # closing_prices = []

    # for i in range(3000):
    #     daily_return_percentages = np.random.normal(
    #         annualized_growth_rate/252, std/math.sqrt(252), 252)+1
    #     price_series = [prices['Close'][0]]
    #     for i in daily_return_percentages:
    #         price_series.append(price_series[-1] * i)

    #     closing_prices.append(price_series[-1])

    # plot all random walks
    # plt.plot(price_series)

    # plt.show()

    # # plot histogram
    # plt.hist(closing_prices, bins=40)

    # plt.show()
# print(total_growth, time_elapsed)
# print(len(prices), total_growth, months_elapsed, monthly_growth_rate,
#       prices['Close'][-1], prices['Close'][0], std)
