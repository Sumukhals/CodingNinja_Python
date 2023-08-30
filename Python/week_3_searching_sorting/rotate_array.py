from sys import stdin


def rotate(arr, n, d):

    rot = d % n
    #Your code goes here
    output_list = []
 
    # Will add values from n to the new list
    for item in range(rot, len(arr)):
        output_list.append(arr[item])
 
    # Will add the values before
    # n to the end of new list
    for item in range(0, rot):
        output_list.append(arr[item])

    for idx in range(len(output_list)):
        arr[idx] = output_list[idx]




#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1