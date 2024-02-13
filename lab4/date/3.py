# Write a Python program to drop microseconds from datetime

# import datetime
from datetime import datetime,timedelta

now = datetime.now()

now_wout_microseconds = now.replace(microsecond=0)

print("Time without microseconds:", now_wout_microseconds)