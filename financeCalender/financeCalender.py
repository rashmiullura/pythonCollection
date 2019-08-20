# Python code to demonstrate the working of
# calendar() function to print calendar

# importing calendar module
# for calendar operations
import calendar

# using calender to print calendar of year
# prints calendar of 2018
print("The calender of year 2018 is : ")
print(calendar.calendar(2018, 2, 1, 6))
cal = calendar.calendar(2109, 1, 1, 1)
print(cal)


# taken from https://www.geeksforgeeks.org/python-calendar-module/
# note sure if this is helpful

# needed is some iterate-able calender, which has a given start-time, then strides over the days

import time

ticks = time.localtime()
# --> ticks: time.struct_time(tm_year=2019, tm_mon=8, tm_mday=20, tm_hour=17, tm_min=1, tm_sec=32, tm_wday=1, tm_yday=232, tm_isdst=1)

print("ticks:", ticks)

# https://o7planning.org/de/11443/anleitung-python-date-time
fakedTime = (2019, 8, 20, 0, 0, 0, 0, 0, 0)
ticks = time.mktime(fakedTime)
print("fakedTime:", fakedTime)
print("ticks:", ticks)

# question: how to jump by "one day"?
# http://www.pressthered.com/adding_dates_and_times_in_python/
from datetime import datetime
from datetime import timedelta
#Pass multiple parameters (1 day and 5 minutes)
print("added 1 d 5 min:", datetime.now() + timedelta(days=1, minutes=5))

# algo:
# read file as input
# determine the "lowest timepoint as start" (eg. current state); maybe sort before the fixed dates
# step with 1 day setting over the time and trigger the actions
