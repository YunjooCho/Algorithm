import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

numbers = []
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

i = 0
j = len(numbers) - 1
cnt = 0
while i < j :
    sum = int(numbers[i]) + numbers[j]
    # print("numbers[%d] : %d, numbers[%d] : %d, sum : %d\n" % (i, numbers[i], j, numbers[j], sum))
    if sum == M : 
        cnt += 1
        i += 1
        j -= 1
        sum = 0
    elif sum > M :
        j -= 1
    elif sum < M :
        i += 1
print(cnt)
