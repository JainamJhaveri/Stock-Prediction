import pandas as pd
import matplotlib.pyplot as plt

def get_specific_data(symbols, daterange):
    df = get_timeindex_df(daterange[0], daterange[-1])
    for symbol in symbols:
        mydata = pd.read_csv("sample_csv_files/{}.csv".format(symbol), index_col='Date', parse_dates=True,
                             usecols=['Date', 'Open'], na_values='nan')
        mydata = mydata.rename(columns={'Open': symbol})
        df = df.join(mydata, how='inner')
    return df


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


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    '''Plot stock prices'''
    # df = normalize(df)
    ax = df.plot(title=title, fontsize=10)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.legend(loc="upper right")
    plt.show()


def plot_selected_data(df, daterange, sp_companies):
    plot_data(df.ix[daterange[0]:daterange[-1], sp_companies], title="Special data")


def get_single_stock_data(symbol, daterange):
    df = get_timeindex_df(daterange[0], daterange[-1])
    mydata = pd.read_csv("sample_csv_files/{}.csv".format(symbol), index_col='Date', parse_dates=True,
                          na_values='nan')
    df = df.join(mydata, how='inner')
    return df
