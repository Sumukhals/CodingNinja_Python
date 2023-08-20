n = int(input())
rowRange = n * 2

startNum = 0
for i in range(1, rowRange):
    for j in range(1, n+1):
        if j > startNum:
            print(j, end="")
        else:
            print(" ", end="")
    if i < n:
        startNum = startNum + 1
    else:
        startNum = startNum - 1
    print()