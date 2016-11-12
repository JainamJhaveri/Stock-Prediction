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


def plot_data(df, title="Stock data"):
    '''Plot stock prices'''
    df = df.ix["'" + enddate + "'":"'" + startdate + "'"]
    df = normalize(df)
    ax = df.plot(title=title, fontsize=10)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def plot_selected_data(df, enddate, startdate, sp_companies):
    plot_data( df.ix[startdate:enddate, sp_companies], title="Special data" )


def normalize(df):
    return df / df.ix[0,:]


if __name__ == '__main__':
    # setting api key for calling quandl apis
    api_key = 'UKT1gkfJ9uwzZouA41hM'
    # setting startdate and enddate for analyzing data
    enddate = datetime.now()
    startdate = enddate - relativedelta(years=5)  # here we can write days=20
    enddate = str(enddate)[:10]
    startdate = str(startdate)[:10]

    main_df = get_timeindex_df(startdate, enddate)
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

    symbols = ['COALIND', 'ICICI', 'KOTAK', 'REL', 'TCS']
    for symbol in symbols:
        mydata = pd.read_csv("sample_csv_files/{}.csv".format(symbol), index_col='Date', parse_dates=True,
                             usecols=['Date', 'Open'], na_values='nan')
        mydata = mydata.rename(columns={'Open': symbol})
        main_df = main_df.join(mydata, how='inner')
    print(main_df)

    # plot_data(df=main_df)
    sp_companies = ['ICICI', 'REL', 'KOTAK']
    plot_selected_data(main_df, startdate, enddate, sp_companies)