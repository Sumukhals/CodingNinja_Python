from sys import stdin

def removeConsecutiveDuplicates(string) :
    # Your code goes here
    retStr = ""
    curChar = '*'
    prevChar = '*'

    for ch in string:
        if ch != curChar:
            retStr = retStr + ch
            curChar = ch
    return retStr
#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)