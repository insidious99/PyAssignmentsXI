# write a program to count the total number of:
# vowels, consonants, digits, and whitespaces in a string

string = input("Enter a string: ")

vowels, consonants, digits, whitespaces = 0, 0, 0, 0

for i in string.lower():
	if i in "aeiou":
		vowels += 1
	elif i in "bcdfghjklmnpqrstvwxyz":
		consonants += 1
	elif i in "0123456789":
		digits += 1
	else:
		whitespaces += 1

print("Vowels: ", vowels)
print("Consonants: ", consonants)
print("Digits: ", digits)
print("Whitespaces: ", whitespaces)