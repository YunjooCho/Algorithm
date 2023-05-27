import sys

numList = []
num = int(sys.stdin.readline())

for _ in range(num) :
	elem = int(sys.stdin.readline())
	numList.append(elem)
numList.sort()

for i in range(num) :
	print(numList[i])