from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    lRowSum = -2147483648
    lColSum = -2147483648

    lColIdx = 0
    lRowIdx = 0
    curSum = 0

    for rowIdx in range(nRows):
        curSum = 0
        for colIdx in range(mCols):
            curSum = curSum + arr[rowIdx][colIdx]

        if curSum > lRowSum:
            lRowSum = curSum
            lRowIdx = rowIdx

    for colIdx in range(mCols):
        curSum = 0
        for rowIdx in range(nRows):
            curSum = curSum + arr[rowIdx][colIdx]

        if curSum > lColSum:
            lColSum = curSum
            lColIdx = colIdx

    if lRowSum >= lColSum:
        print("row", " ", lRowIdx, " ", lRowSum)

    else:
        print("column", " ", lColIdx, " ", lColSum)


#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1