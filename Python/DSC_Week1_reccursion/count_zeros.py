from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def IsPalindromeNumber(num):
    n = num
    if n > 0 and n < 10:
        return 0
    elif n == 0:
        return 1
    newNum = 0
    quotient = 0
    rem = 0
    count = 0
    while n > 0:
        newNum = n % 10
        if newNum == 0:
            count += 1
        n = n // 10

    return count

n = int(input())
retVal = IsPalindromeNumber(n)
print(retVal)