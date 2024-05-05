import sys

maxNum = int(sys.stdin.readline())
operators = []
numbers = []
stack = []
curNum = 1
flag = 0

for i in range(1, maxNum + 1):
		numbers.append(int(sys.stdin.readline()))

for i in range(maxNum):
	if numbers[i] >= curNum:
		while numbers[i] >= curNum:
			stack.append(curNum)
			operators.append("+")
			curNum += 1
		stack.pop()
		operators.append("-")
	else:
		check = stack.pop()
		if check > numbers[i]:
			print("NO")
			flag = 1
			break
		else:
			operators.append("-")

if flag == 0:
	for op in operators:
		print(op)


# idx = len(numbers) - 1
# idx2 = 0
# for n in range(1, maxNum + 1):
# 		if n < numbers[idx]:
# 				stack.append(n)
# 				operators.append("+")
# 		elif n == numbers[idx]:
# 				while len(stack) >= (maxNum - 1 - idx):
# 						if len(stack) == (maxNum - 1 - idx):
# 								stack.append(n)
# 								operators.append("+")
# 								idx -= 1
# 								break
# 						check = stack.pop()
# 						operators.append("-")
# 						if check == numbers[idx2]:
# 								idx2 += 1
# 						else:
# 								print("NO")
# 								exit()
# 		else:
# 						operators.append("-") 

# for i in range(len(stack)):
# 		operators.append("-")
# for op in operators:
# 		print(op)
