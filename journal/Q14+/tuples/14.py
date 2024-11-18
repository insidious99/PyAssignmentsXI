# copy specific items from one tuple to new tuple
tuple1 = (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384)
a, b, c, d, e, f, g, h, i, j, k, l, m, n = tuple1
tuple2 = (a, b, c, d, e, f, g, h, i , j, k, l, m, n)
print(tuple2)