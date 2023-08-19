n = int(input())

startIdx = 1

i = 1
idxToLook = 1
while i <= n:
    j = 1
    if i < (n + 1)//2:
        while j <= n:
            if j == idxToLook:
                k = 1
                while k <= idxToLook:
                    print("*", end="")
                    k = k + 1
                    j = j + 1
            else:
                print(" ", end="")
                j = j + 1
        idxToLook = idxToLook + 1
    else:
        while j <= n:
            if j == idxToLook:
                k = 1
                while k <= idxToLook:
                    print("*", end="")
                    k = k + 1
                    j = j + 1
            else:
                print(" ", end="")
                j = j + 1
        idxToLook = idxToLook - 1

    print()
    i = i + 1