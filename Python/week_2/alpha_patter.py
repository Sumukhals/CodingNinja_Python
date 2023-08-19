## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

i = 0
while i < n:
    j = 0
    while j <= i:
        print(chr(65 + i), end="")
        j = j + 1
    print()
    i = i + 1 