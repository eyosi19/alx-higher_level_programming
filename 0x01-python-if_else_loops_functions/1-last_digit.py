#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number = number % 10

if (number > 5):
    print("{} and is greater than 5".format(number))
elif (number == 0):
    print("{} and is 0".format(number))
elif (number < 6 and number != 0):
    print("{} and is less than 6 and not 0".format(number))
