import math

M, N = map(int, input().split())
primes = []
is_prime = [True] * (N+1)

for i in range(2, int(math.sqrt(N))+1):
    if is_prime[i]:
        for j in range(i*i, N+1, i):
            is_prime[j] = False

for i in range(max(2, M), N+1):
    if is_prime[i]:
        primes.append(i)

for prime in primes:
    print(prime)

