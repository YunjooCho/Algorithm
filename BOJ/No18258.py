import sys
from collections import deque

num = int(sys.stdin.readline())
que = deque()

for _ in range(num):
	inputStr = sys.stdin.readline().rstrip().split()
	if len(inputStr) == 1:
		com = inputStr[0]
	else:
		com, val = inputStr
	
	if com == 'push':
		que.append(int(val))
	elif com == 'pop':
		if len(que) == 0:
			print(-1)
		else:
			print(que.popleft())
	elif com == 'size':
		print(len(que))
	elif com == 'empty':
		if len(que) == 0:
			print(1)
		else:
			print(0)
	elif com == 'front':
		if len(que) == 0:
			print(-1)
		else:
			print(que[0])
	elif com == 'back':
		if len(que) == 0:
			print(-1)
		else:
			print(que[len(que) - 1])