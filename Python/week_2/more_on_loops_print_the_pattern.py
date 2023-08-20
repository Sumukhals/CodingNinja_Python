n =  int(input())

multFact = 1
for i in range(n):
    maxNumInRow = n * multFact
    for j in range((n * (multFact - 1)) + 1, maxNumInRow + 1):
        print(j,end="")
    if maxNumInRow == n * n:
        multFact = 0
    multFact = multFact + 2
    print()