def findItem(arr, x, idx):
    # Please add your code here
    if idx < 0:
        return -1
    if arr[idx] == x:
        return idx

    retVal = findItem(arr, x, idx -1)
    return retVal


def firstIndex(arr, x):
    # Please add your code here
    retVal = findItem(arr, x, len(arr) - 1)
    return retVal

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))