import sys

N, M = map(int, sys.stdin.readline().split())

# numbers = []
# result = []
# sum = 0
# for n in range(0, N) :
#     numbers.append(list(map(int, sys.stdin.readline().split())))

# for m in range(0, M) :
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     for j in range(y1, y2 + 1):
#         for i in range (x1, x2 + 1):
#             sum += numbers[i - 1][j - 1]
#     result.append(sum)
#     sum = 0
# for i in result :
#     print(i)

sums = [[0] * (N + 1) for _ in range(N + 1)] # 위, 왼쪽으로 한 행/열을 추가하여 0으로 초기화
numbers = []
for n in range(N) :
    numbers.append(list(map(int, sys.stdin.readline().split())))

for i in range (1, N + 1) :
    for j in range (1, N + 1) :
        sums[i][j] = sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1] + numbers[i-1][j-1]

for m in range(M) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1]
    print(result)