# input character check if vowel or consonant

c = str(input("Enter a letter: "))

if len(c) > 1:
	print("Invalid input.")
# elif (c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or 
# 	  c == "6" or c == "7" or c == "8" or c == "9" or c == "0"):
	# print("Invalid input")
elif (c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or
	  c == "A" or c == "E" or c == "I" or c == "O" or c == "U"):
	print("Vowel.")
else:
	print("Consonant.")