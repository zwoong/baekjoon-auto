# 입력 받기
N = int(input())
strings = {input() for _ in range(N)}

# 정렬 후 출력
for string in sorted(strings, key=lambda x: (len(x), x)):
    print(string)
