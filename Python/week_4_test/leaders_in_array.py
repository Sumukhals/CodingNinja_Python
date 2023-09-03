## Read input as specified in the question.
## Print output as specified in the question.

numElem = int(input())

elemList = [int(i) for i in input().split()]

# create stack to store leaders
sk = []
sk.append(elemList[numElem - 1])
for i in range(numElem - 2, -1, -1):
    if(elemList[i] >= sk[len(sk) - 1]):
        sk.append(elemList[i])

# print stack elements
# run loop till stack is not empty
while(len(sk) != 0):
    print(sk[len(sk)-1],end = ' ')
    sk.pop()