
def checkMember(n):
    found = True
#Implement Your Code Here
    sPrev = 1
    sNext = 1
    if n == 0:
        return found
        
    while sNext != n:
        temp = sPrev
        sPrev = sNext
        sNext = sNext + temp
        if(sNext > n):
            found = False
            break
    return found

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")