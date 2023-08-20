from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

i = 1
numToFill = 0

while i <= n:
    j = 1
    startEndNum = j + (i - 2)
    if(startEndNum <= 0):
        startEndNum = 1
    while j <= i:
        if(j == 1 or j == i):
            print(startEndNum, end="")
        else:
            print(numToFill, end="")
        j = j + 1
    print()
    i = i + 1