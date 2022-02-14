#2780 

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    num = [1]*10
    for i in range(1, N):
        num0 = num[0]
        num1 = num[1]
        num2 = num[2]
        num3 = num[3]
        num4 = num[4]
        num5 = num[5]
        num6 = num[6]
        num7 = num[7]
        num8 = num[8]
        num9 = num[9]

        num[0] = num7
        num[1] = num2 + num4
        num[2] = num1 + num3 + num5
        num[3] = num2 + num6
        num[4] = num1 + num5 + num7
        num[5] = num2 + num4 + num6 + num8
        num[6] = num3 + num5 + num9
        num[7] = num4 + num8 + num0
        num[8] = num5 + num7 + num9
        num[9] = num6 + num8

    print(sum(num) % 1234567)

