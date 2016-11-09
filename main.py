from urllib.parse import urlencode
from dateutil.relativedelta import relativedelta
from datetime import datetime

cur_dt = datetime.now()
from_dt = cur_dt - relativedelta(years=5)

cur_year = cur_dt.year
cur_month = cur_dt.month -1
cur_day = cur_dt.day

from_year = from_dt.year
from_month = from_dt.month -1
from_day = from_dt.day


# s	Ticker symbol (YHOO in the example)
# a	The "from month" - 1
# b	The "from day" (two digits)
# c	The "from year"
# d	The "to month" - 1
# e	The "to day" (two digits)
# f	The "to year"
# g	d for day, m for month, y for yearly

baseurl = 'http://ichart.finance.yahoo.com/table.csv?'
params = {'s': 'YHOO', 'a': from_month, 'b': from_day, 'c': from_year,
                       'd': cur_month, 'e': cur_day, 'f': cur_year,
           'g': 'd', 'ignore': '.csv'}

print( baseurl + urlencode(params) )