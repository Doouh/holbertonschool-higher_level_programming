#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
cp = number
if (cp < 0):
	cp *= -1
if (cp % 10) > 5:
    if number < 0:
        print("Last digit of {:d} is -{:d} and is greater than 5".format(number, cp % 10))
    else:
        print("Last digit of {:d} is {:d} and is greater than 5".format(number, cp % 10))
elif (cp % 10) == 0:
    if number < 0:
        print("Last digit of {:d} is -{:d} and is 0".format(number, cp % 10))
    else:
        print("Last digit of {:d} is {:d} and is 0".format(number, cp % 10))
elif (cp % 10) < 6:
    if number < 0:
        print("Last digit of {:d} is -{:d} and is less than 6 and not 0".format(number, cp % 10))
    else:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, cp % 10))
