# concatenate two lists index wise
list1 = ['al', 'be', 'ga']
list2 = ['pha', 'ta', 'mma']
ans = list(map(lambda i, j: i + j, list1, list2))
print(ans)
