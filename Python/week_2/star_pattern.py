n = int(input())

totalNumber = (n * 2) - 1

startIdx = 0
numElements = 1
for i in range(1,n+1):
    j = 1
    while j <= totalNumber:
        elementToPrint='*'
        if j == (n-startIdx):
            for k in range(1,numElements+1):
                print(elementToPrint, end="")
                j = j + 1
            numElements = numElements + 2
            print(" ",end="")
        else:
            print(" ",end="")
            j = j + 1
    startIdx = startIdx + 1
    print()
