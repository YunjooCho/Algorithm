import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

mapList = []
virus = []
for i in range(N) :
	mapList.append(list(map(int, sys.stdin.readline().split())))
	for j in range(N) :
		if mapList[i][j] != 0 :
			virus.append((mapList[i][j], 0, i, j))
virus.sort()

S, X, Y = map(int, sys.stdin.readline().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dq = deque(virus)

while dq :
	viNum, seconds, x, y = dq.popleft()
	if seconds == S :
		break
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if nx >= 0 and nx < N and ny >= 0 and ny < N :
			if mapList[nx][ny] == 0 :
				mapList[nx][ny] = viNum
				dq.append((viNum, seconds + 1, nx, ny))
print(mapList[X - 1][Y - 1])