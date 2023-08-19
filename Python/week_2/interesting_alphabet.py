n = int(input())
startChar = ord('A')
startChar = startChar + (n-1)
i = 0
while i < n:
    j = 0
    while j <= i:
        print(chr(startChar - i + j), end="")
        j = j + 1
    print()
    i = i + 1