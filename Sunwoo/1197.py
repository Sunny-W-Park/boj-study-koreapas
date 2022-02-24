#1197

import sys
input = sys.stdin.readline
V, E = map(int, input().split())
INF = int(1e9)
graph = [[INF for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    A, B, C = map(int, input().split())
    graph[A][B] = min(graph[A][B], C)

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[j][k])

result = 0
for i in range(1, V):
    result += graph[i][i+1]

#print(graph)
print(result)

