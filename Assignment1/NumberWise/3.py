# Program to take principal, rate, time and print simple interest

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time period: "))

i = ( p * r * t ) / 100
t = p + i

print("Simple interest for given values is", i)
print("Total amount is", t)
