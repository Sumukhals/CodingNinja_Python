from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def checkAB(string, lookFor, idx, valid):
    if idx == len(string) or valid == False:
        return valid
    if lookFor == "any":
        if string[idx] == 'a':
            lookFor = "any"
        elif string[idx] == 'b':
            lookFor = "b"
    elif lookFor == 'b' and string[idx] == lookFor:
        lookFor = 'a'
    elif lookFor == 'a' and string[idx] == lookFor:
        lookFor = "any"
    else:
        valid = False
    return checkAB(string, lookFor, idx + 1, valid)

string = input()
ret = checkAB(string, 'a', 0, True)

if ret == True:
    print("true")
else:
    print("false")