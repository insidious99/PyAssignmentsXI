# check if input is leap year

# y = int(input("Enter the year: "))
# if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
# 	print(y, "is a leap year.")
# else:
# 	print(y, "is not a leap year.")

import calendar

def checkLeapYear(y):
	return calendar.isleap(y)

y = int(input("Enter the year: "))
print(y, "is a leap year: ", checkLeapYear(y))
