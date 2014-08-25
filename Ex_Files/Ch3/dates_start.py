from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

# print today's date
print "today is: " + str(datetime.now())

today = date.today()  # get today's date
m = date(today.year, 10, 1)  
time_to_afd = abs(m - today)
print time_to_afd.days, "days until m Day!"


