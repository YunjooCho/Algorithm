# 다시 풀기!
import sys
N, M = map(int, input().split())

inputStr = []
for i in range(N):
    inputStr.append(list(map(int, input())))

def dfs(x, y) :
    if x <= -1 or y <= -1 or x >= M or y >= N :
        return False
    if inputStr[y][x] == 0 :
        inputStr[y][x] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

answer = 0
for i in range(N) :
    for j in range(M) : 
        if dfs(j, i) == True :
            answer += 1
print(answer)