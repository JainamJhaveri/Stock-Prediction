from dateutil.relativedelta import relativedelta
from datetime import datetime
from daily_returns import plot_daily_returns, plot_histograms, plot_histograms_detailed
from macd import MACD, plot_macd
from util import get_specific_data, pd, plot_selected_data, plot_data
from bollinger_bands import plot_bollinger_bands


def test_bollinger_bands():
    symbols = ['COALIND', 'ICICI']
    daterange = pd.date_range(startdate, enddate)
    df = get_specific_data(symbols, daterange)
    print(df)
    plot_bollinger_bands(df['COALIND'], 'COALIND')


def test_daily_returns():
    symbols = ['COALIND', 'ICICI']
    daterange = pd.date_range(startdate, enddate)
    df = get_specific_data(symbols, daterange)
    plot_daily_returns(df)


def test_histograms():
    symbols = ['COALIND', 'ICICI']
    daterange = pd.date_range(startdate, enddate)
    df = get_specific_data(symbols, daterange)
    plot_histograms(df, 'ICICI')
    plot_histograms(df, 'COALIND')


def test_histograms_detailed():
    symbols = ['COALIND', 'ICICI']
    daterange = pd.date_range(startdate, enddate)
    df = get_specific_data(symbols, daterange)
    plot_histograms_detailed(df, "ICICI")


def test_macd():
    symbol = ['ICICI']
    daterange = pd.date_range(startdate, enddate)
    df = get_specific_data(symbol, daterange)
    df = MACD(df, 12, 26)
    plot_macd(df, 'ICICI')


if __name__ == '__main__':
    # setting startdate and enddate for analyzing data
    enddate = datetime.now()
    startdate = enddate - relativedelta(days=500)  # here we can write days=20
    enddate = str(enddate)[:10]
    startdate = str(startdate)[:10]

    # test_bollinger_bands()
    # test_daily_returns()
    # test_histograms()
    # test_histograms_detailed()

    test_macd()

    # plot_data(df=df)
