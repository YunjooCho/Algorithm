import sys
import copy

strLen, pwLen = map(int, sys.stdin.readline().rstrip().split())
str = list(sys.stdin.readline().rstrip())
cntList = list(map(int, sys.stdin.readline().rstrip().split()))
check = copy.deepcopy(cntList)

result = 0
i = 0
j = i + (pwLen - 1)

while j < strLen:
	k = i
	# print("i: %d, j: %d" % (i, j))
	while k <= j:
		if str[k] == 'A' and check[0] > 0:
			check[0] -= 1
		elif str[k] == 'C' and check[1] > 0:
			check[1] -= 1
		elif str[k] == 'G' and check[2] > 0:
			check[2] -= 1
		elif str[k] == 'T' and check[3] > 0:
			check[3] -= 1
		# print("str[%d]: %c" % (k, str[k]))
		k += 1
	sum = check[0] + check[1] + check[2] + check[3]
	# print("sum : %d" % sum)
	if sum == 0:
		result += 1
	i += 1
	j += 1
	check = copy.deepcopy(cntList)
print(result)