
import sys

def duplicateNumber(arr, n) :
    sum = 0

    arrSet = set()
    #Your code goes here
    for i in arr:
        if i not in arrSet:
            arrSet.add(i)
        else:
            return i
    
    return sum




#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1