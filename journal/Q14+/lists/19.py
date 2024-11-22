# remove all occurences of a specific item from list
li = [0, 2, 4, 2, 8, 2, 16, 2, 32, 2, 64]
it = 2
print(li)
try: 
    while True:
        li.remove(it)
except ValueError:
    pass
print(li)