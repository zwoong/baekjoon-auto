from collections import deque

num = int(input())

for _ in range(num):
    cnt = 0
    N, M = map(int, input().split())
    imp = deque(map(int, input().split()))

    while True:
        if imp[0] == max(imp):  
            imp.popleft()
            cnt += 1
            if M == 0:  
                break
            else:
                M -= 1
        else:  
            imp.append(imp.popleft())
            if M == 0:
                M = len(imp) - 1
            else:
                M -= 1

    print(cnt)
