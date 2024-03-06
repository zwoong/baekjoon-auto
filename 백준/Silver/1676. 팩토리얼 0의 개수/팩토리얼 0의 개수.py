N = int(input())

count = 0

while N > 0:
    N //= 5
    count += N
print(count)