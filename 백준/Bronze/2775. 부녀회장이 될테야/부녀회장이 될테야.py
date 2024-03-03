T = int(input())

def calculate_residents(k, n):
    zero_floor = [i for i in range(1, n + 1)]

    for _ in range(k):
        for j in range(1, n):
            zero_floor[j] += zero_floor[j - 1]
    return zero_floor[-1]

for _ in range(T):
    k = int(input())  # 층수
    n = int(input())  # 호수
    print(calculate_residents(k, n))
