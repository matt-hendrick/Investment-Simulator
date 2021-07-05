
from pandas_datareader import data as web
import datetime as dt


def getStockPrice(ticker, monthsElapsed=0):

    start = dt.datetime(1970, 1, 1)
    end = dt.datetime.today().strftime("%Y, %m, %d")

    return web.DataReader(ticker, 'stooq', start, end)["Close"][0]


def getStockPriceSeries(ticker, monthsElapsed=0):

    start = dt.datetime(1970, 1, 1)
    end = dt.datetime.today().strftime("%Y, %m, %d")

    return web.DataReader(ticker, 'stooq', start, end)
