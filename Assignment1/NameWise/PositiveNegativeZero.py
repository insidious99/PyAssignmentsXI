# Check if provided number is +, -, or 0

n = int(input("Enter integer: "))

if n > 0:
	print(n, "is positive.")
elif n == 0:
	print(n, "is zero.")
elif n < 0:
	print(n, "is negative.")