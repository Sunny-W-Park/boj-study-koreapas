
#1939

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

start, end = map(int, input().split())
_min, _max = 1, 1000000000

def bfs(c):
    queue = deque()
    queue.append(start)
    visited = set()
    visited.add(start)
    result = 0
    while queue:
        y = queue.popleft()
        for x, w in graph[y]:
            if x not in visited and w >= c:
                visited.add(x)
                queue.append(x)
    if end in visited:
        return True
    else:
        return False

while _min <= _max:
    mid = (_min + _max) // 2
    if bfs(mid):
        result = mid
        _min = mid + 1
    else:
        _max = mid - 1

print(result)
