import sys

A, B, V = map(int, sys.stdin.readline().split())

# days = 0
# distance = 0

# while (1) :
#     days += 1
#     distance += A
#     if distance >= V :
#         break
#     distance -= B
# print(days)

import math

print(math.ceil((V-A)/(A-B)) + 1)
