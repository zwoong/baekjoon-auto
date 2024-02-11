N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for row_a, row_b in zip(A, B):
    result_row = [a + b for a, b in zip(row_a, row_b)]
    print(*result_row)
