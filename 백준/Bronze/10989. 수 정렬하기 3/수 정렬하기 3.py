import sys
input = sys.stdin.readline

n = int(input())
max_value = 10000  
counts = [0] * (max_value + 1)

for _ in range(n):
    num = int(input())
    counts[num] += 1

for i in range(max_value + 1):
    if counts[i] != 0:
        for _ in range(counts[i]):
            print(i)