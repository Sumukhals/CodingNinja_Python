from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    n = nRows # no. of rows
    m = mCols # no. of columns
  
    # Initialize the pointers reqd for traversal.
    top = 0
    left = 0
    bottom = n - 1
    right = m - 1

    # Loop until all elements are not traversed.
    while (top <= bottom and left <= right):
        # For moving left to right
        for i in range(left, right + 1):
            print(mat[top][i], end=" ")

        top += 1

        # For moving top to bottom.
        for i in range(top, bottom + 1):
            print(mat[i][right], end=" ")

        right -= 1

        # For moving right to left.
        if (top <= bottom):
            for i in range(right, left - 1, -1):
                print(mat[bottom][i], end=" ")

            bottom -= 1

        # For moving bottom to top.
        if (left <= right):
            for i in range(bottom, top - 1, -1):
                print(mat[i][left], end=" ")

            left += 1



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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1