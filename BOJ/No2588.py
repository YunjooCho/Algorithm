import sys

nums = []
result = 0
for _ in range(0, 2) :
    nums.append(sys.stdin.readline().strip())
for i in reversed(range(3)) :
    print(int(nums[0]) * int(nums[1][i]))
print(int(nums[0]) * int(nums[1]))
