#9918

import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(6)]
pos = []
x_pos, y_pos = 0, 0
count_x = [0 for _ in range(6)]
count_y = [0 for _ in range(6)]

dx = [-2, 2, 0, 0]
dy = [0, 0, -2, 2]

for i in range(6):
    for j in range(6):
        if arr[i][j] != 0:
            pos.append((i, j, arr[i][j]))
            count_x[i] += 1
            count_y[j] += 1
        if arr[i][j] == 1:
            x_pos = i
            y_pos = j

iscube = False
if (3 in count_x and 4 in count_y) or (4 in count_x and 3 in count_y):
    iscube = True

if iscube == True:
    for i in range(4):
        nx_pos = x_pos + dx[i]
        ny_pos = y_pos + dy[i]
        if 0 <= nx_pos  <= 5 and 0 <= ny_pos <= 5 and arr[nx_pos][ny_pos] != 0:
            print(arr[nx_pos][ny_pos])
else:
    print(0)

