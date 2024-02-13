# Write a Python program to subtract five days from current date.

import datetime
from datetime import timedelta

current_day = datetime.datetime.now()

past_day = current_day - timedelta(days=5)

print("Five days ago:", past_day.strftime("%d-%m-%Y"))

#done