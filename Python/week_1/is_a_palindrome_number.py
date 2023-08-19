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
newNum = 0
while div != 0:
    rem = div % 10
    newNum = newNum + (rem * divMax)
    divMax = divMax // 10
    div = div // 10

if n == newNum:
    print("true")
else:
    print("false")