#11047

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

count = 0

while K != 0:
    for i in range(N-1, -1, -1):
        if K // coins[i] >= 0:
            x = K // coins[i]
            count += x
            K -= x * coins[i]

print(count)

