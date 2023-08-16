#Write Your Code Here
n = int(input())
#find divisor
divMax = 1
div = n
#if n > 10:
while div//10 != 0:
    divMax = divMax * 10
    div = div // 10
div = 10
newNum = 0
while n != 0:
    rem = n % div
    newNum = newNum + (rem * divMax)
    divMax = divMax // 10
    n = n // div
print(newNum)