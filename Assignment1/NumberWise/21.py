# take positive int, output all factors and sum of factors

def findAndSumFactors(n):
	factors = []
	for i in range(1, n + 1):
		if n % i == 0:
			factors.append(i)
	return sum(factors), factors

n = int(input("Enter a positive number: "))
sum, factors = findAndSumFactors(n)

print("The factors of", n, "are:", *factors)
print("The sum of the factors is:", sum)
