# Input principal, rate, time. Output compound interest

p = int(input("Enter principal amount: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter time period: "))

a = p * (1 + (r / 100)) ** t
c = a - p

print("Compound interest =", c)
print("Total amount =", a)
