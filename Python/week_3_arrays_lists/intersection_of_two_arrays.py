
import sys
from itertools import combinations

def intersections(arr1, n, arr2, m) :
    #Your code goes here
    for x in arr1:
        if x in arr2:
            arr2.remove(x)
            print(x, end=" ")



#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1