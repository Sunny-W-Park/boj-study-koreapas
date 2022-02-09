#2156 (1)

import sys
input = sys.stdin.readline

N = int(input())
W = [0]
for i in range(N):
    W.append(int(input()))
dp = [0]
dp.append(W[1])

if N > 1:
    dp.append(W[1] + W[2])

for i in range(3, N+1):
    dp.append(max(dp[i-1], dp[i-3] + W[i-1] + W[i], dp[i-2] + W[i]))

print(dp[N])


#2156 (2)

import sys
input = sys.stdin.readline

N = int(input())
W = [0 for _ in range(10001)]
for i in range(1, N):
    W[i] = int(input())
dp = [0 for _ in range(10001)]

dp[1] = W[1]
dp[2] = W[1] + W[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-2] + W[i], dp[i-3] + W[i-1] + W[i], dp[i-1])

print(dp[N])

