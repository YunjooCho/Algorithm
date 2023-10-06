import sys

N = int(sys.stdin.readline())

cnt = 1
startNum = 1
endNum = startNum
sum = startNum

while endNum != N :
	if sum == N :
		cnt += 1
		endNum += 1
		sum += endNum
	elif sum > N :     # sum을 초기화하고 다시 합계를 구하는 것이 아니라 sum을 가지고 현재 startNum을 빼주면서 N과 동일한 지 확인
		sum -= startNum
		startNum += 1
	else :
		endNum += 1
		sum += endNum
	print("startNum : %d, endNum : %d, sum : %d cnt : %d" % (startNum, endNum, sum, cnt))
print(cnt)

# cnt = 1
# startNum = 1
# endNum = startNum + 1
# sum = startNum
# while startNum < N :
#	sum += endNum
#	# print("startNum : %d, endNum : %d, sum : %d cnt : %d" % (startNum, endNum, sum, cnt))
#	if sum == N :
#		cnt += 1
#	if endNum < N :
#		endNum += 1
#	else :
#		startNum += 1
#		endNum = startNum + 1
#		sum = startNum
# print(cnt)

# while startNum < N :
# 	sum = startNum
# 	endNum = startNum + 1
# 	while sum <= N and endNum <= N :
# 		# print("startNum : %d, endNum : %d, sum : %d cnt : %d" % (startNum, endNum, sum, cnt))
# 		if sum == N :
# 			cnt += 1
# 			break
# 		sum += endNum
# 		endNum += 1
# 	startNum += 1
# print(cnt)
