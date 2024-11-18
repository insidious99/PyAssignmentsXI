# Counts the number of occurrences of item 50 from a tuple.
def count(t, n):
    return t.count(n)
t = (50, 10, 10, 21, 50, 50, 10005, 14, 50, 1, 50)
a = 50
print(count(t, a), "times")