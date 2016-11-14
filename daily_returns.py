from util import *

def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns


def plot_daily_returns(df):
    daily_returns = compute_daily_returns(df)
    print(daily_returns)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")


def plot_histograms(df, symbol):
    daily_returns = compute_daily_returns(df)
    daily_returns[symbol].hist(bins=20, label=symbol)
    plt.legend(loc="upper right")
    plt.show()


def plot_histograms_detailed(df, symbol):
    daily_returns = compute_daily_returns(df)
    daily_returns[symbol].hist(bins=20, label=symbol)
    plt.legend(loc="upper right")
    mean = daily_returns[symbol].mean()
    print("mean: \n" + str(mean))
    std = daily_returns[symbol].std()
    print("std: \n" + str(std))
    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()
