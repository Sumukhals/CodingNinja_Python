from sys import stdin


def isPermutation(string1, string2) :
	#Your code goes here
    inStr = "".join(sorted(string1))
    outStr = "".join(sorted(string2))
    if inStr == outStr:
        return True
    else:
        return False



#main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')
