## Read input as specified in the question
## Print the required output in given format
n = int(input())

i = n
while i > 0:
    j = i
    while j > 0:
        print(i, end="")
        j = j - 1
    print()
    i = i - 1