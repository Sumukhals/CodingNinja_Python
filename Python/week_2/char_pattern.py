n = int(input())
startChar = ord('A')

i = 0
while i < n:
    j = 0
    while j <= i:
        print(chr(startChar + i + j), end="")
        j = j + 1
    print()
    i = i + 1