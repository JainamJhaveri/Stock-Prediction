'''Stochastic oscillator %K, Stochastic oscillator %D'''
import pandas as pd
import matplotlib.pyplot as plt


# Stochastic oscillator %K, Stochastic oscillator %D
def STO(df, n=14):
    SOk = pd.Series((df['Close'] - df['Low']) / (df['High'] - df['Low']))
    SOk = SOk.rename('SO%k')
    SOd = pd.Series(pd.ewma(SOk, span=n, min_periods=n - 1), name='SO%d' + str(n))
    SOd = SOd.rename('SO%d')
    df = df.join(SOk)
    df = df.join(SOd)
    return df


def plot_sto(df, symbol, n=14):
    ax = df['SO%k'].plot(label='SO%k', title="STO Plot for " + symbol)
    df['SO%d' + str(n)].plot(label='SO%d', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Time")
    ax.set_ylabel("SO%k SO%d")
    ax.legend(loc='upper right')
    plt.show()
