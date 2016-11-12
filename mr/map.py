import sys
import quandl
from dateutil.relativedelta import relativedelta
from datetime import datetime

# setting startdate and enddate for analyzing data
enddate = datetime.now()
startdate = enddate - relativedelta(years=5)        # here we can write days=20
enddate = str(enddate)[:10]
startdate = str(startdate)[:10]

# setting api key for calling quandl apis
api_key = 'UKT1gkfJ9uwzZouA41hM'

for line in sys.stdin:
    words = line.split()
    for word in words:
        mydata = quandl.get(dataset=word, api_key=api_key,
                            start_date=startdate, end_date=enddate,
                            collapse="annual",  # can be "daily", "monthly", "weekly", "quarterly", "annual"
                            returns="pandas")  # can be "pandas", "numpy"
        print('%s\t%s' % (word, 1))

