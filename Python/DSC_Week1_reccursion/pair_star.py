from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def replaceStartForRepeats(string, prevChar, idx, newStr):
    if idx == len(string):
        return newStr
    if prevChar == string[idx]:
        newStr = newStr + '*' + string[idx]
    else:
        prevChar = string[idx]
        newStr = newStr + string[idx]

    return replaceStartForRepeats(string, prevChar, idx + 1, newStr)


string = input()
newStr = ''
newStr = replaceStartForRepeats(string, '', 0, newStr)

print(newStr)