# Write a Python program to print yesterday, today, tomorrow.

import datetime
from datetime import timedelta

today = datetime.datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("yesterday -", yesterday.strftime("%d-%m-%Y"), "\ntoday -", today.strftime("%d-%m-%Y"), "\ntomorrow -", tomorrow.strftime("%d-%m-%Y"))

#done