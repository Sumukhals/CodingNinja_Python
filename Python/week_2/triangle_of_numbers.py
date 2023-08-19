n = int(input())

totalNumber = (n * 2) - 1

startIdx = 0
numElements = 1
for i in range(1,n+1):
    j = 1
    while j <= totalNumber:
        elementToPrint=i
        if j == (n-startIdx):
            for k in range(1,numElements+1):
                if(j < n):
                    print(elementToPrint, end="")
                    elementToPrint =  elementToPrint + 1
                else:
                    print(elementToPrint, end="")
                    elementToPrint = elementToPrint - 1
                j = j + 1
            numElements = numElements + 2
            print(" ",end="")
        else:
            print(" ",end="")
            j = j + 1
    startIdx = startIdx + 1
    print()