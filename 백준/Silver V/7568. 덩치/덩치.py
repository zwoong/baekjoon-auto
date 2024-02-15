N = int(input())

people = []
for _ in range(N):
    height, weight = map(int, input().split())
    people.append((height, weight))

result = []
for person1 in people:
    count = 1
    for person2 in people:
        if person1[0] < person2[0] and person1[1] < person2[1]:
            count += 1
    result.append(count)

print(*result)
