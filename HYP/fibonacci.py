# print fibonacci sequence
num = int(input("Enter the number: "))
a, b = 0, 1
count = 0
if num <= 0:
	print("Please enter a positive number")
elif num == 1:
	print("1")
else:
	while count < num:
		print(a)
		c = a + b
		a = b
		b = c
		count += 1