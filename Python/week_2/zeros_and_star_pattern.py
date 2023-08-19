rows = int(input())
cols = (rows * 2) + 1
for i in range(1, rows+1):
        for j in range(1, cols+1):
            if i == j or j == cols - (i - 1):
                print("*", end="")
            elif j == (cols + 1)/2:
                print("*", end="")
            else:
                 print("0", end="")
        print()