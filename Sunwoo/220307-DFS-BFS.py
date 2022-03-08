##### BOJ #####

#7576

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

count_zero = 0
pos_tomato = []

for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            count_zero += 1
        if maps[i][j] == 1:
            pos_tomato.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count_days = 0

if count_zero == 0:
    print(0)

else:
    queue = deque(pos_tomato)
    while len(queue) != 0:
        for k in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                    if maps[nx][ny] == 0:
                        maps[nx][ny] = 1
                        queue.append((nx, ny))
        count_days += 1

    impos = False
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                impos = True

    if impos == True:
        print(-1)
    else:
        print(count_days-1)


#10026

import sys
sys.setrecursionlimit(100000)
from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    l = input()
    for j in range(len(l)):
        graph[i].append(l[j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visited):
    visited[x][y] = 1
    color = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
            if visited[nx][ny] == 0 and graph[nx][ny] == color:
                dfs(nx, ny, visited)

visited = [[0 for _ in range(N)] for _ in range(N)]
count_set1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j, visited)
            count_set1 += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0 for _ in range(N)] for _ in range(N)]
count_set2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j, visited)
            count_set2 += 1

print(count_set1, count_set2)

#7569

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
maps = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
         maps[i].append(list(map(int, input().split())))

dh = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

zero = True

pos = []

for h in range(H):
    for x in range(N):
        for y in range(M):
            if maps[h][x][y] == 0:
                zero = False
            if maps[h][x][y] == 1:
                pos.append((h, x, y))

days = 0

if zero == True:
    print(0)
else:
    q = deque(pos)
    while len(q) > 0:
        for _ in range(len(q)):
            h, x, y = q.popleft()
            for i in range(6):
                nh = h + dh[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nh <= H-1 and 0 <= nx <= N-1 and 0 <= ny <= M-1:
                    if maps[nh][nx][ny] == 0:
                        maps[nh][nx][ny] = 1
                        q.append((nh, nx, ny))
        days += 1

    availability = True
    for h in range(H):
        for x in range(N):
            for y in range(M):
                if maps[h][x][y] == 0:
                    availability = False

    if availability == False:
        print(-1)
    else:
        print(days-1)


n = int(input())

#17265 재풀이

import sys
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(str, input().split())))

dx = [1, 0]
dy = [0, 1]

mv = -(5**25)
nv = 5**25
ops = ["+", "-", "*"]

def dfs(x, y, before, operator):
    global mv
    global nv
    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
            if graph[nx][ny] in ops:
                dfs(nx, ny, before, graph[nx][ny])
            else:
                if operator == '+':
                    dfs(nx, ny, int(before) + int(graph[nx][ny]), '')
                if operator == '-':
                    dfs(nx, ny, int(before) - int(graph[nx][ny]), '')
                if operator == '*':
                    dfs(nx, ny, int(before) * int(graph[nx][ny]), '')
        if nx == N-1 and ny == N-1:
            fv = 0
            if operator == '+':
                fv = int(before) + int(graph[nx][ny])
            if operator == '-':
                fv = int(before) - int(graph[nx][ny])
            if operator == '*':
                fv = int(before) * int(graph[nx][ny])
            mv = max(mv, fv)
            nv = min(nv, fv)

dfs(0, 0, int(graph[0][0]), '')
print(mv, nv)


#17265

import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(str, input().split())))

dx = [1, 0]
dy = [0, 1]

max_answer = -(5**20)
min_answer = 5**20

def dfs(x, y, curr_num, before):
    global max_answer, min_answer

    if x == N-1 and y == N-1:
        max_answer = max(max_answer, int(curr_num))
        min_answer = min(min_answer, int(curr_num))

    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
            if graph[nx][ny].isdigit():
                dfs(nx, ny, str(eval(curr_num + before + graph[nx][ny])), '')
            else:
                dfs(nx, ny, curr_num, graph[nx][ny])

dfs(0, 0, graph[0][0])
print(max_answer, min_answer)

