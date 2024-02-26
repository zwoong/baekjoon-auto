N, M = map(int, input().split())

board = [input() for _ in range(N)]

min_changes = float('inf')

for i in range(N - 7):
  for j in range(M - 7):
    current_changes = 0
    for k in range(8):
      for l in range(8):
        if (k + l) % 2 == 0:
          if board[i + k][j + l] != 'W':
            current_changes += 1
        else:
          if board[i + k][j + l] != 'B':
            current_changes += 1
    min_changes = min(min_changes, current_changes, 64 - current_changes)

print(min_changes)
