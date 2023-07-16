import sys
from collections import deque

list = []
N = int(sys.stdin.readline())
deq = deque(enumerate(map(int,sys.stdin.readline().split())))
if len(deq) != N :
    print("Invalid arguments")
    exit()
while deq:
    idx, val = deq.popleft()
    list.append(idx+1)
    if int(val) >= -N and int(val) <= N:
        if (val > 0):
            deq.rotate(-(val-1))
        elif (val < 0):
            deq.rotate(-val)
print(' '.join(map(str, list)))