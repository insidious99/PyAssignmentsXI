import statistics
import random

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("=== Statistics Module ===")

mean_result = statistics.mean(data)
print(f"Mean of data: {mean_result}")

median_result = statistics.median(data)
print(f"Median of data: {median_result}")

stdev_result = statistics.stdev(data)
print(f"Standard Deviation of data: {stdev_result}")

print("\n=== Random Module ===")

random.shuffle(data)
print(f"Shuffled data: {data}")

random_int = random.randint(1, 100)
print(f"Random integer between 1 and 100: {random_int}")

random_choice = random.choice(data)
print(f"Random choice from data: {random_choice}")
