# check if input number is palindrome

n = input("Enter a number: ")

if n == n[::-1]:
	print(n, "is a palindrome")
else:
	print(n, "is not a palindrome")