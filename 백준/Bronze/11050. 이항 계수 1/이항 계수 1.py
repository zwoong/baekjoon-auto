from math import comb

N, K = map(int, input().split())

binomial_coefficient = comb(N, K)

print(binomial_coefficient)