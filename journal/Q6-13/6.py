# Sum of factorials till num
num = int(input("Enter a number: "))
factorial = 1
sum = 0
for i in range(1, num + 1):
	factorial *= i
	sum += factorial
print(sum)