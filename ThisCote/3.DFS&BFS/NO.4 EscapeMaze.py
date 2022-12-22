
from collections import deque

N, M = map(int, input().split())
mapList = []
cur_x = 0
cur_y = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
  mapList.append(list(map(int, input().rstrip())))

queue = deque()
queue.append((0, 0))

while queue:
  y, x = queue.popleft()
  for i in range(4):
    cur_x = x + dx[i]
    cur_y = y + dy[i]
    if cur_x < 0 or cur_y < 0 or cur_x >= M or cur_y >= N:
      continue
    if mapList[cur_y][cur_x] == 0:
      continue
    if mapList[cur_y][cur_x] == 1:
      mapList[cur_y][cur_x] = mapList[y][x] + 1
      queue.append((cur_y, cur_x))
print(mapList[N-1][M-1])