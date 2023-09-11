def parseEachChars(newString, string, idx):
    if idx == len(string):
        return newString
    if string[idx] != 'x':
        newString = newString + string[idx]
    return parseEachChars(newString, string, idx + 1)


def removeX(string): 
    newString = ""
    newString = parseEachChars(newString, string, 0)
    return newString

# Main
string = input()
print(removeX(string))