# Input two num vars, swap contents WITHOUT using extra var

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: ")
print("Value of a :", a, "and b :", b)

a, b = b, a

print("After swapping: ")
print("Value of a :", a, "and b :", b)

