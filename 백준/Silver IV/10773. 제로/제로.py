K = int(input())

stack = []
for _ in range(K):
    num = int(input())
    if num == 0:
        stack.pop() if stack else None
    else:
        stack.append(num)

print(sum(stack))
