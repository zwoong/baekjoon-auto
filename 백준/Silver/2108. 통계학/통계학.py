import sys
input_func = sys.stdin.readline
n = int(input_func())
data = []
count = {}

_sum = 0
for _ in range(n):
    x = int(input_func())
    data.append(x)
    _sum += x
    count[x] = count.get(x, 0) + 1

data.sort()

print(round(_sum / n))
print(data[n // 2])

mode = max(count.values())
modes = [k for k, v in count.items() if v == mode]

if len(modes) == 1:
    print(modes[0])
else:
    print(sorted(modes)[1])

print(data[-1] - data[0])

