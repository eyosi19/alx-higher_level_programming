#!/usr/bin/python3

for i in range(0, 10):
    for j in range(0 ,10):
        if (i == 9 and j == 9):
            print("99")
            break
        print("{}{}, ".format(i,j), end="")
