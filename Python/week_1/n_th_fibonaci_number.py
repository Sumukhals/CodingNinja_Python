from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

if n==1 or n == 2:
    print(1)
else:
    itr = 3
    prev = 1
    fib = 2
    while itr < n:
        temp = fib
        fib = fib + prev
        prev = temp
        itr = itr + 1
    print(fib)