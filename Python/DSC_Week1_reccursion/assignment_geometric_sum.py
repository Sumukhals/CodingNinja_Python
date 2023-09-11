def findSum(idx, k, sumRes):
    if idx > k:
        return sumRes
    sumRes = sumRes + (1/(pow(2,idx)))
    return findSum(idx + 1, k, sumRes)

k = int(input())
sumRes = 1
res = findSum(1, k, sumRes)
print("{0:.5f}".format(res))