''' MACD, MACD Signal and MACD difference'''
import pandas as pd
import matplotlib.pyplot as plt


# reference: https://www.quantopian.com/posts/technical-analysis-indicators-without-talib-code
def MACD(df, n_fast=12, n_slow=26):
    EMAfast = pd.Series(pd.ewma(df['ICICI'], span=n_fast, min_periods=n_slow - 1))
    EMAslow = pd.Series(pd.ewma(df['ICICI'], span=n_slow, min_periods=n_slow - 1))

    MACD = pd.Series(EMAfast - EMAslow, name='MACD_' + str(n_fast) + '_' + str(n_slow))
    MACDsign = pd.Series(pd.ewma(MACD, span=9, min_periods=8), name='MACDsign_' + str(n_fast) + '_' + str(n_slow))
    MACDdiff = pd.Series(MACD - MACDsign, name='MACDdiff_' + str(n_fast) + '_' + str(n_slow))

    df = df.join(MACD)
    df = df.join(MACDsign)
    df = df.join(MACDdiff)
    df = df.dropna()

    return df

def just_MACD(df, n_fast=12, n_slow=26):
    EMAfast = pd.Series(pd.ewma(df['Open'], span=n_fast, min_periods=n_slow - 1))
    EMAslow = pd.Series(pd.ewma(df['Open'], span=n_slow, min_periods=n_slow - 1))

    MACD = pd.Series(EMAfast - EMAslow)
    MACD = MACD.rename('MACD')
    df = df.join(MACD)
    return df


def plot_macd(df, symbol):
    # ax = df[symbol].plot(title="MACD Plot for " + symbol, label=symbol)
    ax = df['MACD_12_26'].plot(label='MACD_12_26', title="MACD Plot for " + symbol)
    df['MACDsign_12_26'].plot(label='MACDsign_12_26', ax=ax)
    df['MACDdiff_12_26'].plot(label='MACDdiff_12_26', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Time")
    ax.set_ylabel("MACD")
    ax.legend(loc='upper right')
    plt.show()
