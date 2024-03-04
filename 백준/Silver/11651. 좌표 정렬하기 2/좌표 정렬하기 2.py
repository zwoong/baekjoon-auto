N = int(input())

coordinates = [tuple(map(int, input().split())) for _ in range(N)]
coordinates.sort(key=lambda coord: (coord[1], coord[0]))

for x, y in coordinates:
    print(x, y)
