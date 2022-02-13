#1149

N = int(input())
C = []
for i in range(N):
    C.append(list(map(int, input().split())))
for i in range(1, len(C)):
    C[i][0] = min(C[i-1][1], C[i-1][2]) + C[i][0]
    C[i][1] = min(C[i-1][0], C[i-1][2]) + C[i][1]
    C[i][2] = min(C[i-1][0], C[i-1][1]) + C[i][2]

print(min(C[N-1]))

