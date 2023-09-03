from sys import stdin


def highestOccuringChar(string) :

	highCount = 0
	highChar = ''
	ma = {}

	#Your code goes here
	for ch in string:
		if ch in ma:
			ma[ch] = ma[ch] + 1
		else:
			ma[ch] = 1

	highChar= max(ma, key = ma.get)

	return highChar



#main
string = stdin.readline().strip()
ans = highestOccuringChar(string)

print(ans)