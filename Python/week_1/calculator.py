while True:
    opr = int(input())
    if opr > 6 or opr == 0:
        print("Invalid Operation")
    elif opr == 1:
        a = int(input())
        b = int(input())
        print(a+b)
    elif opr == 2:
        a = int(input())
        b = int(input())
        print(a-b)
    elif opr == 3:
        a = int(input())
        b = int(input())
        print(a*b)
    elif opr == 4:
        a = int(input())
        b = int(input())
        print(a//b)
    elif opr == 5:
        a = int(input())
        b = int(input())
        print(a%b)
    elif opr == 6:
        break