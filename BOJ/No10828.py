import sys

que = []
num = int(sys.stdin.readline())

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
			print(que.pop(len(que) - 1))
	elif com == 'size':
		print(len(que))
	elif com == 'empty':
		if len(que) == 0:
			print(1)
		else:
			print(0)
	elif com == 'top':
		if len(que) == 0:
			print(-1)
		else:
			print(que[len(que) - 1])