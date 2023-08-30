
from sys import stdin

def arrayRotateCheck(arr, n):
    #Your code goes here
    rotCount = 0

    for idx in range(len(arr) - 1):
        if arr[idx + 1] < arr[idx]:
            rotCount = idx + 1
            break
    return rotCount





#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(arrayRotateCheck(arr, n))

    t -= 1