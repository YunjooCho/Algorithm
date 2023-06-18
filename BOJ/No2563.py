import sys

cnt = int(sys.stdin.readline())
matrix = [[0] * 100 for _ in range(100)]

for _ in range(cnt) :
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10) :
        for j in range(y, y + 10) :
            matrix[i][j] = 1

result = 0
for num in matrix :
    result += num.count(1)
print(result)