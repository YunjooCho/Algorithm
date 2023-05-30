import sys

min, max = map(int, sys.stdin.readline().split())

def isPrime(num):
	if num == 1 :
		return False
	else :
		for i in range(2, int(num**0.5) + 1): #num의 제곱근만큼만 확인
			if (num % i == 0) :
				return False
		return True

for i in range(min, max + 1) :
	if isPrime(i) :
		print(i)