N = int(input())

Coordinates = [list(map(int, input().split())) for i in range(N)]
Coordinates.sort()

for row in Coordinates:
  print(*row)
