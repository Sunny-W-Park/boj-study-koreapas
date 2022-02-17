#1246

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = []
for _ in range(M):
    P.append(int(input()))
P = sorted(P, reverse = True)

result = 0
price = 0

for i in range(M):
    if i <= N-1:
        if result < (i+1) * P[i]:
            result = (i+1) * P[i]
            price = P[i]

print(price, result)
