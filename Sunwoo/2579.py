#2579

import sys
input = sys.stdin.readline

N = int(input())
S = [0 for _ in range(301)]
for i in range(N):
    S[i] = int(input())

dp = [0 for _ in range(301)]
dp[0] = S[0]
dp[1] = S[0] + S[1]
dp[2] = max(S[0]+S[2], S[1]+S[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + S[i-1] + S[i], dp[i-2] + S[i])

print(dp[N-1])

