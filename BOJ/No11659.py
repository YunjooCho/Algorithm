import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
sums = []
sums.append(0)
for i in range(0, len(numbers)):
    sum = sums[i] + numbers[i]
    sums.append(sum)
for _ in range(0, M) :
    i, j = map(int, sys.stdin.readline().split())
    print(sums[j] - sums[i-1])