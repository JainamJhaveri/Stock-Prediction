from csv import reader
import quandl
from dateutil.relativedelta import relativedelta
from datetime import datetime
import pandas as pd
import numpy as np

# setting startdate and enddate for analyzing data
enddate = datetime.now()
startdate = enddate - relativedelta(years=5)
enddate = str(enddate)[:10]
startdate = str(startdate)[:10]

# reading csv file of nse-dataset-codes
csv_file = open("NSE-datasets-codes.csv")
csv_rows = list(reader(csv_file))
rows = len(csv_rows)

# setting api key for calling quandl apis
quandl.ApiConfig.api_key = 'UKT1gkfJ9uwzZouA41hM'

# for each stock do the following
# for i in range(0, rows):
for i in range(0, 1):
    url = csv_rows[i][0]
    print(url)
    mydata = quandl.get(url, start_date=startdate, end_date=enddate, collapse="annual", returns="pandas")
    print(mydata)