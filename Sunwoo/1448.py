#1448

import sys
input = sys.stdin.readline

N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))
num = sorted(num)

result = 0

for i in range(N-1, 1, -1):
    if num[i] < num[i-1] + num[i-2]:
        result = num[i] + num[i-1] + num[i-2]
        break

if result == 0:
    print(-1)
else:
    print(result)
