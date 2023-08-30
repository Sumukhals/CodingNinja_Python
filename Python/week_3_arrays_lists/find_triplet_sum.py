
from sys import stdin
from itertools import combinations

def findTriplet(arr, n, x) :
    #Your code goes here
    #return your answer
    triplet_count = 0

    def valid(val):
        return sum(val) == x
         
    final_temp_list =  list(filter(valid, list(combinations(arr, 3))))

    return len(final_temp_list)






#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n



#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(findTriplet(arr, n, x))
    t -= 1