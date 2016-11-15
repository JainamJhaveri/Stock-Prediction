from dateutil.relativedelta import relativedelta
from datetime import datetime
from daily_returns import plot_daily_returns, plot_histograms, plot_histograms_detailed
from macd import *
from stochastic import *
from util import get_specific_data, pd, plot_selected_data, plot_data, get_single_stock_data
from bollinger_bands import *
from moving_averages import *
# from sklearn import linear_model, datasets
# import scipy

def test_bollinger_bands():
    symbols = ['COALIND']
    daterange = pd.date_range(startdate, enddate)
    df = get_specific_data(symbols, daterange)
    # print(df)
    plot_bollinger_bands(df['COALIND'], 'COALIND')

def test_sim_moving_average():
    symbols = ['COALIND']
    daterange = pd.date_range(startdate, enddate)
    df = get_specific_data(symbols, daterange)
    # print(df)
    plot_sim_moving_average(df['COALIND'], 'COALIND')

def test_exp_moving_average():
    symbols = ['COALIND']
    daterange = pd.date_range(startdate, enddate)
    df = get_specific_data(symbols, daterange)
    # print(df)
    plot_exp_moving_average(df['COALIND'], 'COALIND')

# def test_daily_returns():
#     symbols = ['COALIND', 'ICICI']
#     daterange = pd.date_range(startdate, enddate)
#     df = get_specific_data(symbols, daterange)
#     plot_daily_returns(df)
#
#
# def test_histograms():
#     symbols = ['COALIND', 'ICICI']
#     daterange = pd.date_range(startdate, enddate)
#     df = get_specific_data(symbols, daterange)
#     plot_histograms(df, 'ICICI')
#     plot_histograms(df, 'COALIND')
#
#
# def test_histograms_detailed():
#     symbols = ['COALIND', 'ICICI']
#     daterange = pd.date_range(startdate, enddate)
#     df = get_specific_data(symbols, daterange)
#     plot_histograms_detailed(df, "ICICI")


def test_macd():
    symbol = ['ICICI']
    daterange = pd.date_range(startdate, enddate)
    df = get_specific_data(symbol, daterange)
    df = MACD(df, 12, 26)
    plot_macd(df, 'ICICI')


def test_sto():
    symbol = 'ICICI'
    daterange = pd.date_range(startdate, enddate)
    df = get_single_stock_data(symbol, daterange)
    print(df)
    df = STO(df)
    print(df)
    plot_sto(df, symbol)


def get_training_data(symbol):

    daterange = pd.date_range(startdate, enddate)
    df = get_single_stock_data(symbol, daterange)

    df = simple_moving_average(df)
    df = exponential_moving_average(df)
    df = STO(df)
    df = just_MACD(df)
    df = df.ix[:,[0,7,8,9,10,11]]
    print(df)
    return df

if __name__ == '__main__':
    # setting startdate and enddate for analyzing data
    enddate = datetime.now() - relativedelta(years=1)
    startdate = enddate - relativedelta(years=4)  # Get 4 years of data for training
    enddate = str(enddate)[:10]
    startdate = str(startdate)[:10]

    df = get_training_data('COALIND')



    # Plotting individual indicators
    # test_bollinger_bands()
    # test_daily_returns()
    # test_histograms()
    # test_histograms_detailed()
    # test_macd()
    # test_sto()
    # test_exp_moving_average()

    # plot_data(df=df)

