def myFunc(e):
  return len(e)

inString = input()
inStrList = inString.split()

inStrList.sort(key=myFunc)

print(inStrList[0])
