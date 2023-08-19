n = int(input())

totalNumber = n

startIdx = (n+1)//2
numElements = 1
for i in range(1,n+1):
    j = 1
    if i < (n+1)//2:
        while j <= totalNumber:
            elementToPrint='*'
            if j == startIdx:
                for k in range(1,numElements+1):
                    print(elementToPrint, end="")
                    j = j + 1
                numElements = numElements + 2
            else:
                print(" ",end="")
                j = j + 1
        startIdx = startIdx - 1
    else:
        while j <= totalNumber:
            elementToPrint='*'
            if j == startIdx:
                for k in range(1,numElements+1):
                    print(elementToPrint, end="")
                    j = j + 1
                numElements = numElements - 2
            else:
                print(" ",end="")
                j = j + 1
        startIdx = startIdx + 1
    print()
