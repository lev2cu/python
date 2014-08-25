from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime



today = date.today()  # get today's date
get_red = date(today.year, 10, 3)
get4m = abs(get_red - today)
print "Getting ready to fly: ", get4m

md  = date(today.year, 10, 10)
tim4m = abs(md - today)
print "getting everything done:",tim4m

