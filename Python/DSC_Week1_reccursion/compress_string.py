def compressString(string, prevChar, charCount, idx, newStr):
    if idx == len(string):
        return newStr

    if string[idx] == prevChar:
        charCount += 1
    else:
        charCount = 1
        prevChar = string[idx]
        newStr = newStr + string[idx]

    return compressString(string, prevChar, charCount, idx + 1, newStr)

    

def removeConsecutiveDuplicates(string):
    # Please add your code here
    newString = ''
    newString = compressString(string, ' ', ' ', 0, newString)

    return newString

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))