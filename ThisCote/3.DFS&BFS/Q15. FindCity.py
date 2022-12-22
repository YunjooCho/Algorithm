import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

adjList = [[] for _ in range(N + 1)]
checkList = [-1 for _ in range(N + 1)]
checkList[X] = 0

for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    adjList[a].append(b)

dq = deque()
dq.append(X)

cnt = 0
while dq :
    cur_node = dq.popleft()
    for next_node in adjList[cur_node] :
        if checkList[next_node] == -1 :
            checkList[next_node] = checkList[cur_node] + 1
            dq.append(next_node)

answer = False
for i in range(1, N + 1) :
    if checkList[i] == K :
        print(i)
        answer = True
if answer == False : 
    print(-1)


#mapList = []
#answer = []
#for i in range(M) :
#    mapList.append(list(map(int, sys.stdin.readline().rstrip().split())))

#cnt = 0
#i = 0
#while dq :
#    #print(dq)
#    popped = dq.popleft()
#    for i in range(M) : 
#        if mapList[i][0] == popped :
#            for j in range(i + 1, M) :
#                print(j, mapList[j][1], end=' ')
#                if mapList[i][1] == mapList[j][0] :
#                    print("OK")
#                    ##print(j, mapList[j][1])
#                    #dq.append(mapList[i][1])
#                    #cnt += 1
#                else :
#                    print("NG")
                #    #print(j, mapList[j][1])
                #    break
    #if cnt == K:
    #    break