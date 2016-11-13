from csv import reader
import quandl
from dateutil.relativedelta import relativedelta
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


# create custom time data-frame
def get_timeindex_df(mystartdate, myenddate):
    """Return dataframe of requested dataset from Quandl.
    :rtype: DataFrame
    """
    dates = pd.date_range(mystartdate, myenddate)
    # df = pd.DataFrame(index=dates)
    df = pd.DataFrame({"Date": dates})
    df['Date'] = df['Date'].apply(lambda x: x.date())
    df = pd.DataFrame(index=df.Date)
    return df


def get_company_code_csv_as_list():
    # reading csv file of nse-dataset-codes
    csv_file = open("NSE-datasets-codes.csv")
    csv_rows = list(reader(csv_file))
    return csv_rows


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    '''Plot stock prices'''
    # df = normalize(df)
    ax = df.plot(title=title, fontsize=10)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def plot_selected_data(df, startdate, enddate, sp_companies):
    plot_data(df.ix[startdate:enddate, sp_companies], title="Special data")


def normalize(df):
    return df / df.ix[-1, :]


def get_specific_data(symbols, daterange):
    df = get_timeindex_df(daterange[0], daterange[-1])
    for symbol in symbols:
        mydata = pd.read_csv("sample_csv_files/{}.csv".format(symbol), index_col='Date', parse_dates=True,
                             usecols=['Date', 'Open'], na_values='nan')
        mydata = mydata.rename(columns={'Open': symbol})
        df = df.join(mydata, how='inner')
    return df


def get_rolling_mean(values, window):
    return pd.Series.rolling(values, window=window).mean()


def get_rolling_std(values, window):
    return pd.Series.rolling(values, window=window).std()


def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    upper_band = rm + 2 * rstd
    lower_band = rm - 2 * rstd
    return upper_band, lower_band


def plot_bollinger_bands(singledf, symbol):
    # 1. Compute rolling mean
    rm = get_rolling_mean(singledf, window=10)

    # 2. Compute rolling standard deviation
    rstd = get_rolling_std(singledf, window=10)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm, rstd)

    # Plot raw values, rolling mean and Bollinger Bands
    ax = singledf.plot(title="Bollinger Bands for "+symbol, label=symbol)
    rm.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


def compute_daily_returns(df):
    daily_returns = (df/df.shift(1)) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns


if __name__ == '__main__':
    # setting api key for calling quandl apis
    api_key = 'UKT1gkfJ9uwzZouA41hM'
    # setting startdate and enddate for analyzing data
    enddate = datetime.now()
    startdate = enddate - relativedelta(days=100)  # here we can write days=20
    enddate = str(enddate)[:10]
    startdate = str(startdate)[:10]

    # main_df = get_timeindex_df(startdate, enddate)
    # csv_rows = get_company_code_csv_as_list()
    #
    # for i in range(0, 3):
    #     companycode = csv_rows[i][0]
    #     print(companycode)
    #     mydata = quandl.get(dataset=companycode, api_key=api_key,
    #                         start_date=startdate, end_date=enddate,
    #                         collapse="annual",  # can be "daily", "monthly", "weekly", "quarterly", "annual"
    #                         returns="pandas")  # can be "pandas", "numpy"
    #     mydata = mydata[['High']]
    #     mydata = mydata.rename(columns={'High': companycode[4:]})
    #     print(mydata)
    #
    #     main_df = main_df.join(mydata, how='inner')
    #     print(main_df)
    # plot_data(df=main_df)

    # symbols = ['TCS']
    symbols = ['COALIND', 'ICICI']
    daterange = pd.date_range(startdate, enddate)
    df = get_specific_data(symbols, daterange)

    # plot_bollinger_bands(df['TCS'], 'TCS')

    print(df)
    # plot_data(df)
    daily_returns = compute_daily_returns(df)
    print(daily_returns)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    # print(df)
    # plot_data(df=df)
