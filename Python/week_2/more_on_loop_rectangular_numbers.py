n = int(input())

numRows = (n * 2) - 1

for i in range(1, numRows + 1):
    if i <= n:
        for j in range(1, i + 1):
            printNum = n - (j - 1)
            print(printNum, end="")
    else:
        for j in range(1, i + 1):
            
            print(n - (j - 1), end="")
    print()
        