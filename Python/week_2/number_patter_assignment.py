n = int(input())

i = 1
numCol = n * 2
while i <= n:
    j = 1
    while j <= numCol:
        if j == 1 or j == (numCol-(i-1)):
            if(j == 1):
                k = 1
                while k <= i:
                    print(k, end="")
                    k = k + 1
                    j = j+1
            else:
                k = i
                while k >= 1:
                    print(k, end="")
                    k = k - 1
                    j = j + 1
        else:
            print(" ", end="")
            j = j + 1
    print()
    i = i + 1