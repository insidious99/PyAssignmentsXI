def Pascal():
	rows = int(input("Enter the number of rows: "))
	coef = 1
	for i in range(1, rows+1):
		for space in range(1, rows-i+1):
			print(" ", end="")
		for j in range(0, i):
			if j == 0 or i == 0:
				coef = 1
			else:
				coef = coef * (i-j)//j
			print(coef, end=" ")
		print()
def Floyd():
	rows = int(input("Enter the number of rows: "))
	num = 1
	for i in range(1, rows+1):
		for j in range(1, i+1):
			print(num, end=" ")
			num += 1
		print()
Floyd()