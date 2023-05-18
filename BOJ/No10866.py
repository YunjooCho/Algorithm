from collections import deque
import sys

deque = deque()
com, arg = int(sys.stdin.readline().split())
print(com)
print(arg)

def push_front(X) :
	deque.appendleft(X)

def push_back(X) :
	deque.append(X)

def pop_front() :
	deque.popleft()

def pop_back() :
	deque.pop()