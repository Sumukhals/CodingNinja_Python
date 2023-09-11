from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def IsPalindromeNumber(num):
    n = num
    if n > 0 and n < 10:
        return n
    newNum = 0
    quotient = 0
    rem = 0
    while n > 0:
        newNum = newNum + (n % 10)
        n = n // 10

    return newNum

n = int(input())
retVal = IsPalindromeNumber(n)
print(retVal)