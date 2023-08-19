n = int(input())

i = 1
numToFill = 2

while i <= n:
    j = 1
    startEndNum = 1
    while j <= i:
        if(j == 1 or j == i):
            print(startEndNum, end="")
        else:
            print(numToFill, end="")
        j = j + 1
    print()
    i = i + 1