n = int(input())

inc = 1
flag = True
for i in range(1,n+1):
    rRange = n * inc
    if rRange  < (n*n) and flag:
        for j in range(rRange - (n - 1),rRange + 1):
            print(j, end=" ")
        inc = inc + 2
    elif rRange == (n * n):
        flag = False
        for j in range(rRange - (n - 1),rRange + 1):
            print(j, end=" ")
        inc = inc - 1
    else:
        flag = False
        if rRange > (n * n):
            inc = inc - 1
            rRange = n * inc
        for j in range(rRange - (n - 1),rRange + 1):
            print(j, end=" ")
        inc = inc - 2        
    print()