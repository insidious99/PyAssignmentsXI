# fibonacci series till n terms
num = int(input("Enter a number: "))
a, b = 0, 1
count = 0
while count < num:
	print(a)
	c = a + b
	a = b
	b = c
	count += 1
	