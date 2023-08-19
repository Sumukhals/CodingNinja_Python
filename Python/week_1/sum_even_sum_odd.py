n=int(input())  
# taking n as a input 
## write your code !!
retVal = False
divMax = 1
div = n
#if n > 10:
while div//10 != 0:
    divMax = divMax * 10
    div = div // 10
div = n
evenSum = 0
oddSum = 0
while div != 0:
    rem = div % 10
    if rem % 2 == 0:
        evenSum = evenSum + rem
    else:
        oddSum = oddSum + rem
    divMax = divMax // 10
    div = div // 10
print(evenSum, " ", oddSum)