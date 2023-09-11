from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def findStep(n):
    if ( n == 0 ):
        return 1
    elif (n < 0):
        return 0
 
    else:
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)
 
 
# Driver code
n = int(input())
print(findStep(n))