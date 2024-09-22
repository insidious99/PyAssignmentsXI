def Pyramid():
	rows = int(input("Enter the number of rows: "))
	for i in range(rows):
		for j in range(i+1):
			print("*", end=" ")
		print()
def PyramidNum():
	rows = int(input("Enter the number of rows: "))
	for i in range(rows):
		for j in range(i+1):
			print(j+1, end=" ")
		print()
def PyramidAlpha():
	rows = int(input("Enter the number of rows: "))
	for i in range(rows):
		for j in range(i+1):
			ascii_value = 65
			alphabet = chr(ascii_value)
			print(alphabet, end="")
		ascii_value += 1
		print()
