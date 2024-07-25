# input marks of 3 subs, find grade

x = float(input("Enter your marks in Subject 1: "))
y = float(input("Enter your marks in Subject 2: "))
z = float(input("Enter your marks in Subject 3: "))

a = round((x + y + z) / 3, 2)

if x or y or z > 100:
	print("Invalid input.")
elif x or y or z < 0:
	print("Invalid input.")
elif a >= 90:
	print("Average: ", a)
	print("Grade A")
elif a >= 80:
	print("Average: ", a)
	print("Grade B")
elif a >= 70:
	print("Average: ", a)
	print("Grade C")
elif a >= 60:
	print("Average: ", a)
	print("Grade D")
elif a < 60:
	print("Average: ", a)
	print("Grade F")
else:
	print("Invalid input.")