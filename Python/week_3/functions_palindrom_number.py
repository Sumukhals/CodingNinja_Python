def IsPalindromeNumber(num):
    n = num
    if n > 0 and n < 10:
        return True
    newNum = 0
    quotient = 0
    rem = 0
    while n > 0:
        newNum = newNum * 10
        newNum = newNum + (n % 10)
        n = n // 10

    if(num == newNum):
        return True
    return False

n = int(input())
retVal = IsPalindromeNumber(n)
if retVal:
    print("true")
else:
    print("false")
