from csv import reader
import quandl
from dateutil.relativedelta import relativedelta
from datetime import datetime
from util import get_timeindex_df, plot_data


def get_company_code_csv_as_list():
    # reading csv file of nse-dataset-codes
    csv_file = open("NSE-datasets-codes.csv")
    csv_rows = list(reader(csv_file))
    return csv_rows

if __name__ == '__main__':
    # setting api key for calling quandl apis
    api_key = 'UKT1gkfJ9uwzZouA41hM'
    # setting startdate and enddate for analyzing data
    enddate = datetime.now()
    startdate = enddate - relativedelta(years=5)  # here we can write days=20
    enddate = str(enddate)[:10]
    startdate = str(startdate)[:10]

    main_df = get_timeindex_df(startdate, enddate)
    print(main_df)
    csv_rows = get_company_code_csv_as_list()

    for i in range(10, 12):
        companycode = csv_rows[i][0]
        print(companycode)
        mydata = quandl.get(dataset=companycode, api_key=api_key,
                            start_date=startdate, end_date=enddate,
                            collapse="daily",  # can be "daily", "monthly", "weekly", "quarterly", "annual"
                            returns="pandas")  # can be "pandas", "numpy"
        print(mydata)
        mydata = mydata[['High']]
        mydata = mydata.rename(columns={'High': companycode[4:]})
        print(mydata)

        main_df = main_df.join(mydata, how='inner')
        print(main_df)
    plot_data(df=main_df)