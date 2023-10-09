import sys

N = int(sys.stdin.readline())

S = set()
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()

for k in range(N):
	i = 0
	j = N - 1
	while i < j:
		if (arr[i] + arr[j]) == arr[k]:
			if i != k and j != k:
				S.add(arr[k])
				break
			elif i == k:
				i += 1
			elif j == k:
				j -= 1
		elif (arr[i] + arr[j]) < arr[k]:
			i += 1
		else:
			j -= 1
print(len(S))