#11052

import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))
C = [0]
for i in range(N):
    C.append(B[i])
dp = [0 for _ in range(N+1)]

dp[1] = C[1]

for i in range(2, N+1):
    for j in range(1, i+1):
        if dp[i] < dp[i-j] + C[j]:
            dp[i] = dp[i-j] + C[j]
print(dp[N])

