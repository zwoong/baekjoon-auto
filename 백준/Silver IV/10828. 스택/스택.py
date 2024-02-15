import sys

def push(stack, element):
    stack.append(element)

def pop(stack):
    if not stack:
        return -1
    return stack.pop()

def size(stack):
    return len(stack)

def empty(stack):
    return 1 if not stack else 0

def top(stack):
    return stack[-1] if stack else -1

N = int(input())
stack = []

for _ in range(N):
    command = sys.stdin.readline().rstrip()
    if "push" in command:
        element = command.split()[1]
        push(stack, element)
    elif "pop" in command:
        print(pop(stack))
    elif "size" in command:
        print(size(stack))
    elif "empty" in command:
        print(empty(stack))
    elif "top" in command:
        print(top(stack))
