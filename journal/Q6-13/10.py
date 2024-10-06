# check odd/eve bw 1 to 10k
odd, eve = 0, 0
for i in range(1, 10001):
	if i % 2 == 0:
		eve += 1
	else: 
		odd += 1
print("Number of odd numbers: ", odd)
print("Number of even numbers: ", eve)