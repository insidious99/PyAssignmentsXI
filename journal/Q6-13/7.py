# print:
# *
# * *
# * * *
# * * * *
# ...... no. of rows
rows = int(input("Enter the number of rows: "))
for a in range(rows):
	for b in range(a + 1):
		print("*", end = " ")
	print()