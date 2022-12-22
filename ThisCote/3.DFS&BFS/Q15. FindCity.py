import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

mapList = []
answer = []
for i in range(M) :
    mapList.append(list(map(int, sys.stdin.readline().rstrip().split())))

dq = deque()
dq.append(X)

cnt = 0
i = 0
while dq :
    popped = dq.popleft()
    cnt += 1
    for i in range(M) : 
        if mapList[i][0] == popped :
            for j in range(i+1, M) :
                if mapList[i][1] == mapList[j][0] :
                    dq.append(mapList[i][1])
                    break 
            print(dq)
            print(cnt)
    if cnt == K:
        break
    i += 1

# def dfs(X) :
#     for i in range(M) : 
#         if mapList[i][0] == X :
#             dfs(mapList[i][1])
#             return i
#     return -1

# cnt = 0
# for _ in range(K) :
#     result = dfs(X)
#     if result == -1 :
#         print(-1)
#     else :
#         cnt += 1
#         if cnt == K :
#             print(result)