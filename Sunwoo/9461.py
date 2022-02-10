#9461

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(5, 101):
    dp[i] = dp[i-5] + dp[i-1]

for i in range(N):
    print(dp[arr[i]])

