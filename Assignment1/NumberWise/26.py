# print first 25 numbers of fibonacci sequence

n = 25
a = 0
b = 1
next = b
count = 1

while count <= n:
	print(next, end="\n")
	count += 1
	a, b = b, next
	next = a + b

print()