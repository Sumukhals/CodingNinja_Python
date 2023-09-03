from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)


def getCompressedString(input) :
	# Write your code here.
	index = 0
	compressed = ""
	len_str = len(input)
	while index != len_str:
		count = 1
		while (index < len_str-1) and (input[index] == input[index+1]):
			count = count + 1
			index = index + 1
		if count == 1:
			compressed += str(input[index])
		else:
			compressed += str(input[index]) + str(count)
		index = index + 1
	return compressed




# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)