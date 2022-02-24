#11403 재풀이

N = int(input())
g = []
for _ in range(N):
    g.append(list(map(int, input().split())))

def dfs(i):
    for j in range(N):
        if visited[j] == 0 and g[i][j] == 1:
            visited[j] = 1
            dfs(j)

visited = [0 for _ in range(N)]
for i in range(N):
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end = " ")
        if visited[j] == 0:
            print(0, end = " ")
    print()
    visited = [0 for _ in range(N)]


