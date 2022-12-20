import sys

S = set()
num = int(input())

for _ in range(num):
	inputStr = sys.stdin.readline().rstrip().split()
	if len(inputStr) == 1 :
		com = inputStr[0]
	else :
		com, val = inputStr

	if com == 'add' : #if 'add' in com : 가 조금 더 느림
		S.add(int(val))
	elif com == 'remove' :
		if int(val) in S :
			S.remove(int(val))
	elif com == 'check' :
		if int(val) in S :
			print(1)
		else : 
			print(0)
	elif com == 'toggle' :
		if int(val) in S :
			S.remove(int(val))
		else : 
			S.add(int(val))
	elif com == 'all' :
		S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
	elif com == 'empty' :
		S.clear()