n = int(input())
numStr = input()
li = []

i = 1
sum = 0
numStrSplit = numStr.split()

for num in numStrSplit:
    sum += int(num)

print(sum)
