def printTable(s,e,w):

	while s <= e:
                s32 = s - 32
                cel = int((s32 * (5/9)))
                print(s,cel,sep="  ")
                s = s + w

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)