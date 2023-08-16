s = int(input())
e = int(input())
w = int(input())

while s < e:
    s32 = s - 32
    cel = int((s32 * (5/9)))
    print(s,cel,sep=" ")
    s = s + w