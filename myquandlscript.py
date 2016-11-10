from csv import reader
import quandl
from dateutil.relativedelta import relativedelta
from datetime import datetime

# setting startdate and enddate for analyzing data
enddate = datetime.now()
startdate = enddate - relativedelta(years=5)        # here we can write days=20
enddate = str(enddate)[:10]
startdate = str(startdate)[:10]

# reading csv file of nse-dataset-codes
csv_file = open("NSE-datasets-codes.csv")
csv_rows = list(reader(csv_file))
rows = len(csv_rows)

# setting api key for calling quandl apis
api_key = 'UKT1gkfJ9uwzZouA41hM'

# for each stock do the following
# for i in range(0, rows):
for i in range(0, 1):
    companycode = csv_rows[i][0]
    print(companycode)
    mydata = quandl.get(dataset=companycode, api_key=api_key,
                        start_date=startdate, end_date=enddate,
                        collapse="annual",          # can be "daily", "monthly", "weekly", "quarterly", "annual"
                        returns="numpy")            # can be "pandas", "numpy"
    print(mydata)


                        # The headers are as follows:
# ---------------------------------------------------------------------------------
#   Date    Open   High   Low   Last  Close  Total Trade-Quantity  Turnover(Lacs)
# ---------------------------------------------------------------------------------