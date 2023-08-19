from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

i = n

while i > 0:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()