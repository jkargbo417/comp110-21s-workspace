"""A vaccination calculator."""

__author__ = "730333820"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population = int(input("Enter population "))
doses_admin = int(input("Enter total number of doses administered "))
doses_per_day = int(input("Enter the number of doses given each day "))
target_percent = int(input("Enter the target percent of the population "))
date = datetime.today()
how_many_days = (((population / 100) * target_percent) - (doses_admin /2)) / (doses_per_day / 2)
completion_date = timedelta(how_many_days)  + date
how_many_days = int(how_many_days)
completion_date = completion_date.strftime("%B %d, %Y")
print("We will reach",str(target_percent) + "% vaccination in",str(how_many_days),"days, which falls on",str(completion_date) + ".")

