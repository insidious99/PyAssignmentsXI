# input number, output first n terms of series formed by squares

n = int(input("Enter a positive number: "))

for i in range(1, n + 1):
	print(i ** 2)