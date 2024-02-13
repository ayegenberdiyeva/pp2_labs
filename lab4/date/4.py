# Write a Python program to calculate two date difference in seconds.

from datetime import datetime, timedelta

def difference(date_1, date_2):
    if date_1>date_2:
        return abs(date_1 - date_2).total_seconds()
    elif date_2>date_1:
        return abs(date_2-date_1).total_seconds()
    return 0

date_1 = datetime(int(input("First date\nYear: ")), int(input("Month: ")), int(input("Day: ")))
date_2 = datetime(int(input("Second date\nYear: ")), int(input("Month: ")), int(input("Day: ")))

print(difference(date_1, date_2))

#done