import sys

T = int(sys.stdin.readline())

def bfs(i, j, arr, check, M, N):
	que = []
	que.append((i, j))
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]

	while que:
		y, x = que.pop(0)
		for idx in range(4):
			cur_y = y + dy[idx]
			cur_x = x + dx[idx]
			if cur_x < 0 or cur_y < 0 or cur_x >= M or cur_y >= N or check[cur_y][cur_x] == 1 or arr[cur_y][cur_x] == 0:
				continue
			else:
				check[cur_y][cur_x] = 1
				que.append((cur_y, cur_x))

for _ in range(T):
	cnt = 0
	M, N, K = map(int, sys.stdin.readline().split())
	arr = [[0] * M for _ in range(N)]
	check = [[0] * M for _ in range(N)]

	for _ in range(K):
		X, Y = map(int, sys.stdin.readline().split())
		arr[Y][X] = 1

	for i in range(N):
		for j in range(M):
			if arr[i][j] == 1 and check[i][j] != 1:
				check[i][j] = 1
				bfs(i, j, arr, check, M, N)
				cnt += 1
	print(cnt)