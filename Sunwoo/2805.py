#2805

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

start = 0
end = nums[-1]
arr = []

while start <= end:
    result = 0
    mid = (start + end) // 2
    for i in nums:
        if i > mid:
            result += i - mid
    if result >= M:
        arr.append(mid)
        start = mid + 1
    else:
        end = mid - 1

print(arr[-1])


