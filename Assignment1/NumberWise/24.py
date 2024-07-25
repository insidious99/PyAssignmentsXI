# take input number and reverse its digits

def reverseNumber(number):
	original = number
	reverse = 0

	for _ in str(number):
		digit = number % 10
		reverse = reverse * 10 + digit
		number //= 10

	print("Original number: ", original)
	print("Reversed number: ", reverse)

number = int(input("Enter a number: "))
reverseNumber(number)