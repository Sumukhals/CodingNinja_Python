from sys import stdin

def pushZerosAtEnd(arr, n) :
    #Your code goes here

    retList = []
    zeroCount = 0

    for num in arr:
        if num != 0:
            retList.append(num)
        else:
            zeroCount += 1
    
    for idx in range(zeroCount):
        retList.append(0)

    for idx in range(len(arr)):
        arr[idx] = retList[idx]

    return retList



#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
  

#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1