from os import *
from sys import *
from collections import *
from math import *

n , m = input().split()

mat=[[int(j) for j in input().split()] for i in range(int(n))]

for rowIdx in range(int(n)):
    for printIdx in range((int(n)- rowIdx)):
        for colIdx in range(int(m)):
            print(mat[rowIdx][colIdx], end=" ")
        print()