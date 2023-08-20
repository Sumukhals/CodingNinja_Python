n = int(input())

startNum = 1
for i in range(1, n + 1):
    for j in range(0, n - (i - 1)):
        print(startNum, end="")
    else:
        startNum = startNum ^ 1
    print()