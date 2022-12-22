import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

mapList = []
for _ in range(N) :
	mapList.append(list(map(int, sys.stdin.readline().split())))
testList = [[0] * N for _ in range(N)]

S, X, Y = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque()

#bfs
def virus(x, y, viNum, time) :
	if mapList[x][y] == 0 or viNum < mapList[x][y]:
		mapList[x][y] = viNum
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if nx >= 0 and nx < N and ny >= 0 and ny < N :
			if mapList[nx][ny] == 0:
				dq.append((nx, ny, viNum, time+1))

for x in range(N):
	for y in range(N):
		if mapList[x][y]:
			dq.append((x,y,mapList[x][y], 0))

while dq:
	x, y, viNum, time = dq.popleft()
	if time > S:
		break
	virus(x, y, viNum, time)

##dfs
#def searchValue(viNum)	:
#	if viNum == K + 1 :
#		return
#	for i in range(N) :
#		for j in range(N) :
#			testList[i][j] = mapList[i][j]
#	for i in range(N) :
#		for j in range(N) : 
#			if mapList[i][j] == viNum :
#				dq.append((i, j))
#				virus(i, j, viNum)
#	searchValue(viNum + 1)
for row in mapList:
	print(row)

#while dq :

#	for i in range(4) :

#searchValue(1)

def key(var):
	return len(var)

[abc, a, qwe, qweqa]
[3, 1, 3, 4]
arr.sort(key=key)