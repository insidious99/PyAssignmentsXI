import statistics
import random

# Sample data for demonstration
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# === Statistics Module ===
print("=== Statistics Module ===")

# 1. Mean
mean_result = statistics.mean(data)
print(f"Mean of data: {mean_result}")

# 2. Median
median_result = statistics.median(data)
print(f"Median of data: {median_result}")

# 3. Standard Deviation
stdev_result = statistics.stdev(data)
print(f"Standard Deviation of data: {stdev_result}")

# === Random Module ===
print("\n=== Random Module ===")

# 1. Random float between 0 and 1
random.shuffle(data)
print(f"Shuffled data: {data}")

# 2. Random integer within a range
random_int = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_int}")

# 3. Random choice from a list
random_choice = random.choice(data)
print(f"Random choice from data: {random_choice}")