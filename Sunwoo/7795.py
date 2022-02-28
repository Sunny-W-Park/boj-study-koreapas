#7795

import sys
import bisect

input = sys.stdin.readline 

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    count = 0
    num_A = list(map(int, input().split()))
    num_A = sorted(num_A)
    num_B = list(map(int, input().split()))
    for i in num_B:
        idx = bisect.bisect_right(num_A, i)
        count += len(num_A) - idx 
    print(count)
