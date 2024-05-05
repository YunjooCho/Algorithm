num = input()
cnt = 0

while len(num) > 1:
	num = str(sum(list(map(int, num))))
	cnt += 1
print(cnt)
if int(num) % 3 == 0:
	print("YES")
else:
	print("NO")

# import sys

# num = int(sys.stdin.readline())
# sum = 0
# cnt = 1

# while (1):
# 	if (num < 10):
# 		num = sum + num
# 		sum = num
# 		if (sum < 10):
# 			break
# 		else:
# 			sum = 0
# 			cnt = cnt + 1
# 	sum = sum + (num % 10)
# 	num = num//10
# print(cnt)
# if (num % 3 == 0):
# 	print("YES")
# else:
# 	print("NO")