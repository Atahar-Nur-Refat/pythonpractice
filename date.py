#Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
# Legal Format Codes for Date and Time in Python

# %a  - Weekday, short version (e.g., Wed)
# %A  - Weekday, full version (e.g., Wednesday)
# %w  - Weekday as a number (0-6, where 0 is Sunday)
# %d  - Day of the month (01-31)
# %b  - Month name, short version (e.g., Dec)
# %B  - Month name, full version (e.g., December)
# %m  - Month as a number (01-12)
# %y  - Year, short version without century (e.g., 18)
# %Y  - Year, full version (e.g., 2018)
# %H  - Hour (00-23, 24-hour format)
# %I  - Hour (00-12, 12-hour format)
# %p  - AM/PM indicator
# %M  - Minute (00-59)
# %S  - Second (00-59)
# %f  - Microsecond (000000-999999)
# %z  - UTC offset (e.g., +0100)
# %Z  - Timezone (e.g., CST)
# %j  - Day number of the year (001-366)
# %U  - Week number of the year (Sunday as the first day of the week, 00-53)
# %W  - Week number of the year (Monday as the first day of the week, 00-53)
# %c  - Local version of date and time (e.g., Mon Dec 31 17:41:00 2018)
# %C  - Century (e.g., 20)
# %x  - Local version of date (e.g., 12/31/18)
# %X  - Local version of time (e.g., 17:41:00)
# %%  - A literal % character
# %G  - ISO 8601 year (e.g., 2018)
# %u  - ISO 8601 weekday (1-7, where 1 is Monday)
# %V  - ISO 8601 week number (01-53)
