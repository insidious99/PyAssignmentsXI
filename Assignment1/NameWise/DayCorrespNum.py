# input 1 to 7, return day corresponding to num, 1-sun, 7-sat

def daysOfTheWeek(dayNumber):
	days = {
		1: "Sunday",
		2: "Monday",
		3: "Tuesday",
		4: "Wednesday",
		5: "Thursday",
		6: "Friday",
		7: "Saturday"
	}
	if dayNumber in days:
		return days[dayNumber]
	else:
		return "Invalid input."

try:
	dayNumber = int(input("Enter a number between 1 and 7: "))
except ValueError:
	print("Invalid input.")
	exit()

dayOfWeek = daysOfTheWeek(dayNumber)
print(dayOfWeek)