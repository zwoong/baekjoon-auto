import sys
input = sys.stdin.readline

def round_half_up(num):
    return int(num + 0.5)

n = int(input())
ban = round_half_up(n * 0.15)

if n == 0:
    print(0)
else:
    scores = [int(input()) for _ in range(n)]
    scores.sort()

    total_score = sum(scores[ban:n-ban])
    avg_score = total_score / (n - 2 * ban)
    print(round_half_up(avg_score))
