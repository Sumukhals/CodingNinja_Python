from sys import stdin


def pairSum(arr, n, x) :
    m = [0] * 1000
 
    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1
 
    twice_count = 0
 
    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):
 
        twice_count += m[x - arr[i]]
 
        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (x - arr[i] == arr[i]):
            twice_count -= 1
 
    # return the half of twice_count
    return int(twice_count / 2)





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
    print(pairSum(arr, n, x))

    t -= 1