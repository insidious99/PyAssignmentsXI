# import the math module and use any 10 mathematical functions to perform operations
import math

num = float(input("Enter a number: "))

sqrt_result = math.sqrt(num)
print(f"Square root of {num}: {sqrt_result}")

log_result = math.log(num)
print(f"Natural logarithm of {num}: {log_result}")

log10_result = math.log10(num)
print(f"Logarithm (base 10) of {num}: {log10_result}")

ceil_result = math.ceil(num)
print(f"Ceiling of {num}: {ceil_result}")

floor_result = math.floor(num)
print(f"Floor of {num}: {floor_result}")

power_result = math.pow(num, 2)  # Squaring the number
print(f"{num} raised to the power of 2: {power_result}")

radians_result = math.radians(num)
print(f"{num} degrees in radians: {radians_result}")

sin_result = math.sin(num)
print(f"Sine of {num} radians: {sin_result}")

cos_result = math.cos(num)
print(f"Cosine of {num} radians: {cos_result}")

tan_result = math.tan(num)
print(f"Tangent of {num}: {tan_result}")