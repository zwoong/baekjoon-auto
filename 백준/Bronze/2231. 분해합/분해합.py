n = int(input())

for i in range(1, n + 1):
    num_sum = i + sum(map(int, str(i))) 
    if num_sum == n:
        print(i)
        break
else: 
    print(0)
