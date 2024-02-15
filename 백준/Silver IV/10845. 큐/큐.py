import sys
from collections import deque

def push(dq, element):
    dq.append(element)

def pop(dq):
    return dq.popleft() if dq else -1

def size(dq):
    return len(dq)

def empty(dq):
    return 1 if not dq else 0

def front(dq):
    return dq[0] if dq else -1

def back(dq):
    return dq[-1] if dq else -1

N = int(input())
dq = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == "push":
        push(dq, command[1])
    elif command[0] == "pop":
        print(pop(dq))
    elif command[0] == "size":
        print(size(dq))
    elif command[0] == "empty":
        print(empty(dq))
    elif command[0] == "front":
        print(front(dq))
    elif command[0] == "back":
        print(back(dq))
