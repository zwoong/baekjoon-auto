L = int(input())
r = 31
M = 1234567891

hash_value = 0
input_string = input()

for i in range(L):
    hash_value += (ord(input_string[i]) - ord('a') + 1) * (r ** i)

print(hash_value % M)
