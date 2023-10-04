def contains(s,t):
    #Implement This Function Here
    # if length of the b = 0
    # then we return true
    if len(t) == 0:
        return True
 
    # if length of a = 0
    # that means b is not present in
    # a so we return false
    if len(s) == 0:
        return False
 
    if(s[0] == t[0]):
        return contains(s[1:], t[1:])
    else:
        return contains(s[1:], t)
    
s = input()
t = input()

ans = contains(s,t)
if ans is True:
    print('true')
else:
    print('false')