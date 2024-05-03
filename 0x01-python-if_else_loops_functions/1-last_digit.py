#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number < 0):
    n = -number % 10
else:
    n = number % 10

if (n > 5):
    print("Last digit of {} is {} and is greater than 5".format(number, n))
elif (n == 0):
    print("Last digit of {} is {} and is 0".format(number, n))
elif (n < 6 and n != 0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, n))
