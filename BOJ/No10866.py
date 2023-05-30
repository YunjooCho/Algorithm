from collections import deque
import sys

deque = deque()
cnt = int(sys.stdin.readline())
for _ in range(cnt) :
	inputStr = sys.stdin.readline().rstrip().split()
	if len(inputStr) == 1 :
		com = inputStr[0]
	else :
		com, X = inputStr
  
	if com == 'push_front' :
		deque.appendleft(X)
	elif com == 'push_back' :
		deque.append(X)
	elif com == 'pop_front' :
		if (len(deque) == 0) :
			print(-1)
		else :
			print(deque.popleft())
	elif com == 'pop_back' :
		if (len(deque) == 0) :
			print(-1)
		else :
			print(deque.pop())
	elif com == 'size' :
		print(len(deque))
	elif com == 'empty' :
		if (len(deque) == 0) :
			print(1)
		else :
			print(0)
	elif com == 'front' :
		if (len(deque) == 0) :
			print(-1)
		else :
			print(deque[0])
	elif com == 'back' :
		if (len(deque) == 0) :
			print(-1)
		else :
			print(deque[len(deque) - 1])
