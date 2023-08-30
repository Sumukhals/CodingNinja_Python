import sys

def secondLargestElement(arr, n):
    larg = -1
    sLarg = -1

    for ele in arr:
        if ele > larg:
            sLarg = larg
            larg = ele
        elif ele > sLarg:
            sLarg = ele
    else:
        if sLarg == -1:
            sLarg = larg

    return sLarg   



def takeInput() :
    n = int(sys.stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#main
arr, n = takeInput()
print(secondLargestElement(arr, n))