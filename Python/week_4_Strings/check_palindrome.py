inStr = input()

paliStr = inStr[len(inStr): : -1]

if inStr == paliStr:
    print("true")
else:
    print("false")