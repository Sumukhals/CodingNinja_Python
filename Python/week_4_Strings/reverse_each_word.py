from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
	resString = ""
	splitLst = string.split()

	for curStr in splitLst:
		resString = resString + curStr[len(curStr) - 1: :-1]
		resString = resString + " "

	return resString




#main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)