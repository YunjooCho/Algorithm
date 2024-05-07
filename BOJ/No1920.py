import sys

N = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().rstrip().split()))
nList.sort()
M = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(M):
	for j in range(N):
		if mList[i] == nList[j]:
			print(1)
			break
		elif j == len(nList) - 1:
			print(0)