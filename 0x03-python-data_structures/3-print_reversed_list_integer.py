#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    j = len(my_list)
    if j == 0:
        pass
    else:
        for i in range(j - 1, -1, -1):
            print("{:d}".format(my_list[i]))