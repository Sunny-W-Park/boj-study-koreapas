#2075 N번째 큰 수 

import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    nums = list(map(int, input().split()))
    if len(heap) == 0:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])

#1461 도서관 

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
book = list(map(int, input().split()))

plus = []
minus = []
count = []

for i in book:
    if i > 0:
        plus.append(i)
    else:
        minus.append(abs(i))

plus.sort(reverse = True)
minus.sort(reverse = True)

for i in range(len(plus)//M):
    count.append(plus[i*M])
if len(plus) % M > 0:
    count.append(plus[len(plus)//M * M])

for i in range(len(minus)//M):
    count.append(minus[i*M])
if len(minus) % M > 0:
    count.append(plus[len(minus)//M * M])

count.sort()

result = count.pop()
result += 2*sum(count)
print(result)

#2212 센서

import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
s = list(map(int, input().split()))
s.sort()

dp = [0 for _ in range(N-1)]
for i in range(N-1):
    dp[i] = s[i+1]-s[i]
dp.sort()

result = 0
for i in range(N-1-(K-1)):
    result += dp[i]

print(result)

#2170 선 긋기

import sys
input = sys.stdin.readline
N = int(input())
lines = []
for _ in range(N):
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort()

set_a, set_b = 0, 0
result = 0
for i in range(N):
    if i == 0:
        set_a, set_b = lines[i][0], lines[i][1]
        result += set_b - set_a
    else:
        new_a, new_b = lines[i][0], lines[i][1]
        #새로운 선 그리는 경우
        if new_a >= set_b:
            result += new_b - new_a
            set_a, set_b = new_a, new_b
        #기존 선에서 연장하는 경우
        if new_a < set_b and new_b > set_b:
            result += new_b - set_b
            set_b = new_b
        #기존 선에 겹쳐 그리는 경우
        if new_a >= set_a and new_b <= set_b:
            continue

print(result)

#13164 행복유치원

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stds = list(map(int, input().split()))
stds.sort()
dp = [0] * (N-1)
for i in range(N-1):
    dp[i] = stds[i+1] - stds[i]

dp.sort()
result = 0
for j in range(len(dp)-(K-1)):
    result += dp[j]
print(result)


