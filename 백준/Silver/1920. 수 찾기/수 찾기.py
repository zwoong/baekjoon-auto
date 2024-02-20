N = int(input())
target_numbers = set(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))


result = [1 if num in target_numbers else 0 for num in numbers]

for r in result:
    print(r)