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
