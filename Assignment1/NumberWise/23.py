# check armstrong number

n = int(input("Enter a number: "))
s = n  
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1 + (r ** b)
    n = n // 10
if s == sum1:
    print(s, "is an armstrong number")
else:
    print(s, "is not an armstrong number")