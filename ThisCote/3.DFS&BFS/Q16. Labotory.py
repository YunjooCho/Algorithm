# 다시 풀기!
import sys

N, M = map(int, sys.stdin.readline().split())

mapList = []
testList = [[0] * M for _ in range(N)]

for _ in range(N) :
	mapList.append(list(map(int, sys.stdin.readline().split())))

dx = [ -1, 1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]

result = 0

def virus(x, y) :
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if nx >= 0 and nx < N and ny >= 0 and ny < M :
			if testList[nx][ny] == 0 :
				testList[nx][ny] = 2
				virus(nx, ny)

def get_area() :
	area = 0
	for i in range(N) :
		for j in range(M) :
			if testList[i][j] == 0 :
				area += 1
	return area

def dfs(count) :
	global result

	if count == 3 :
		for i in range(N) :
			for j in range(M) : 
				testList[i][j] = mapList[i][j]
		for i in range(N) :
			for j in range(M) :
				if testList[i][j] == 2 :
					virus(i, j)
		result = max(result, get_area())
		return
	for i in range(N) : 
		for j in range(M) :
			if mapList[i][j] == 0 :
				mapList[i][j] = 1
				count += 1
				dfs(count)
				mapList[i][j] = 0
				count -= 1
dfs(0)
print(result)