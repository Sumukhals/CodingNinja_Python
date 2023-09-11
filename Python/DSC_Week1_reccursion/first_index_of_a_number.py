def firstIndex(arr, x):
    # Please add your code here
    retVal = -1
    try:
        retVal = arr.index(x)
    except:
        retVal = -1
    return retVal

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))
