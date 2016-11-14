from csv import reader
import quandl
from dateutil.relativedelta import relativedelta
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from util import get_specific_data, plot_data


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
    ax = singledf.plot(title="Bollinger Bands for " + symbol, label=symbol)
    rm.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()
