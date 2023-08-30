from os import *
from sys import *
from collections import *
from math import *

n = int(input())

i = 1
j = n
while i <= n:
    j = n
    while j >= 1:
        if j == i:
            print("*", end="")
        else:
            print(j, end="")
        j = j - 1
    print()
    i = i + 1