import sys

n1 = int(sys.stdin.readline())
n2 = int(sys.stdin.readline())

if n1 > 0:
	if n2 > 0:
		print(1)
	else:
		print(4)
else:
	if n2 > 0:
		print(2)
	else:
		print(3)

