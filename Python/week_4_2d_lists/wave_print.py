from sys import stdin

def wavePrint(mat, nRows, mCols):
    #Your code goes here
    isDown = True

    for colIdx in range(mCols):
        if isDown:
            for rowIdx in range(nRows):
                print(mat[rowIdx][colIdx], end=" ")
        else:
            for rowIdx in reversed(range(nRows)):
                print(mat[rowIdx][colIdx], end=" ")

        isDown = isDown ^ True

#Taking Iput Using Fast I/O
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
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1