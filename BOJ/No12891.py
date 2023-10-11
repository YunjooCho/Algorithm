import sys

strLen, pwLen = map(int, sys.stdin.readline().rstrip().split())
inputStr = list(sys.stdin.readline().rstrip())
reqList = list(map(int, sys.stdin.readline().rstrip().split()))
curList = [0] * 4
standVal = 0
result = 0

def addElem(c):
	global reqList, curList, standVal
	if c == 'A':
		curList[0] += 1
		if curList[0] == reqList[0]:
			standVal += 1
	elif c == 'C':
		curList[1] += 1
		if curList[1] == reqList[1]:
			standVal += 1
	elif c == 'G':
		curList[2] += 1
		if curList[2] == reqList[2]:
			standVal += 1
	elif c == 'T':
		curList[3] += 1
		if curList[3] == reqList[3]:
			standVal += 1

def delElem(c):
	global reqList, curList, standVal
	if c == 'A':
		if curList[0] == reqList[0]:
			standVal -= 1
		curList[0] -= 1
	elif c == 'C':
		if curList[1] == reqList[1]:
			standVal -= 1
		curList[1] -= 1
	elif c == 'G':
		if curList[2] == reqList[2]:
			standVal -= 1
		curList[2] -= 1
	elif c == 'T':
		if curList[3] == reqList[3]:
			standVal -= 1
		curList[3] -= 1

for idx in range(4):
	if reqList[idx] == 0:
		standVal += 1
for i in range(pwLen):
	addElem(inputStr[i])
if standVal == 4:
	result += 1

for i in range(pwLen, strLen):
	j = i - pwLen
	addElem(inputStr[i])
	delElem(inputStr[j])
	if standVal == 4:
		result += 1
print(result)