#!/usr/bin/python3
for i in range(9):
    j = 1
    for j in range(10):
        if (i == 8 and j == 9):
            print("{}{}".format(i, j))
            break
        if (i < j):
            print("{}{}, ".format(i, j), end='')