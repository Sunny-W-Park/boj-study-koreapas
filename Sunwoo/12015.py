#12015

import sys
import bisect
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

arr = [0]

for i in A:
    if arr[-1] < i:
        arr.append(i)
    else:
        arr[bisect.bisect_left(arr, i)] = i

print(len(arr)-1)
