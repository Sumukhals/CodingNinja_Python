def search(nums: [int], target: int):
    # write your code logic !!
    try:
        retVal = nums.index(target)
    except:
        retVal = -1
    return retVal


   
n= int (input())
arr = list(map(int,input().strip().split()))[:n]
target =int (input())
print (search(arr, target))