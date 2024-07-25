# Take seconds and convert in hrs, mins, secs

import datetime

s = int(input("Enter time in seconds: "))
t = str(datetime.timedelta(seconds=s))

print(t)

