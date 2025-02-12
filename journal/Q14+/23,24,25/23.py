# Check if given number is perfect number using UDF
def is_perfect_number(n):
    if n <= 0:
        return False
    
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    
    return divisors_sum == n

num = int(input("Enter a number to check if it's a perfect number: "))

if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")