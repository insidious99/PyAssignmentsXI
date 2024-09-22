n = str(input("Enter your name: "))
s = int(input("Enter your class: "))
r = int(input("Enter your roll number: "))
a = int(input("Enter the marks of subject 1: "))
b = int(input("Enter the marks of subject 2: "))
c = int(input("Enter the marks of subject 3: "))
d = int(input("Enter the marks of subject 4: "))
e = int(input("Enter the marks of subject 5: "))

sum = a + b + c + d + e
avg = sum / 5
per = round((sum / 500) * 100, 2)

print("Name: ", n)
print("Class: ", s)
print("Roll number: ", r)
print("Average marks: ", avg)
print("Percentage: ", per)
