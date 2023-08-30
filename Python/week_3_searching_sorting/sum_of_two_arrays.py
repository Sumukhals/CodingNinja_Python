from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    num1 = 0
    num2 = 0
    outLen = len(output)
    #Your code goes here
    for idx in range(len(arr1)):
        num1 += arr1[idx] * pow(10, (n - (idx +1)))

    for idx in range(len(arr2)):
        num2 += arr2[idx] * pow(10, (m - (idx +1)))


    sumVal = num1 + num2

    numElem = 0
    while sumVal > 0:
        rem = sumVal % 10
        output.insert(0, rem)
        sumVal = sumVal // 10
        numElem += 1

    while numElem < outLen:
        output.insert(0,0)
        numElem += 1




#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = " ")
    
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1