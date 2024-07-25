# input positive int, output sum of digits of int

def sumOfDigits(n):
	if n < 0:
		print("Input a positive number.")

	sum = 0
	while n > 0:
		digit = n % 10
		sum += digit
		n //= 10
	return sum

while True:
	try:
		n = int(input("Enter a positive number: "))
		if n > 0:
			break
		else:
			print("Input a positive number.")
	except ValueError:
		print("Input a positive number.")

sum = sumOfDigits(n)
print("The sum of the digits of", n, "is", sum)