# Input principal, rate, time. Output compound interest

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time period: "))

a = p * (1 + (r / 100)) ** t
c = a - p

print("Compound interest =", c)
print("Total amount =", a)
