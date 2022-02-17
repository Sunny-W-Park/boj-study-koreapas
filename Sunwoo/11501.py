#11501 재풀이

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    profit = 0
    price = list(map(int, input().split()))
    m = price[-1]
    for i in range(N-1, -1, -1):
        if price[i] < m:
            profit += m - price[i]
        else:
            m = max(m, price[i])
    print(profit)

#11501

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    profit = [0] * N
    price = list(map(int, input().split()))
    for i in range(N-1):
        if price[i] < max(price[i+1:]):
            profit[i] += max(price[i+1:]) - price[i]
    print(sum(profit))



