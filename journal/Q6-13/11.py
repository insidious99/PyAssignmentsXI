# print the letter A in a pattern
size = 7
width = size

for row in range(size):
    for col in range(width):
        is_border = (col == 0 or col == width - 1) and row != 0
        is_top = row == 0 and col % 2 == 1
        is_middle = row == size // 2 and col % 2 == 0
        
        if is_border or is_top or is_middle:
            print("*", end="")
        else:
            print(" ", end="")
    print()


