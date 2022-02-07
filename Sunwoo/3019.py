#3019

import sys
input = sys.stdin.readline
C, P = map(int, input().split())
pos = list(map(int, input().split()))

result = 0

if P == 1:
    result += C
    for i in range(C-3):
        if pos[i] == pos[i+1] and pos[i+1] == pos[i+2] and pos[i+2] == pos[i+3]:
            result += 1

if P == 2:
    for i in range(C-1):
        if pos[i] == pos[i+1]:
            result += 1

if P == 3:
    for i in range(C-1):
        if pos[i] == pos[i+1] + 1:
            result += 1
    for i in range(C-2):
        if pos[i] == pos[i+1] and pos[i+1] == pos[i+2] - 1:
            result += 1

if P == 4:
    for i in range(C-2):
        if pos[i] == pos[i+1] + 1 and pos[i+1] == pos[i+2]:
            result += 1
    for i in range(C-1):
        if pos[i] == pos[i+1] - 1:
            result += 1

if P == 5:
    for i in range(C-2):
        if pos[i] == pos[i+1] and pos[i+1] == pos[i+2]:
            result += 1
        if pos[i] == pos[i+1] + 1 and pos[i+1] == pos[i+2] - 1:
            result += 1
    for i in range(C-1):
        if pos[i] == pos[i+1] - 1:
            result += 1
        if pos[i] == pos[i+1] + 1:
            result += 1

if P == 6:
    for i in range(C-2):
        if pos[i] == pos[i+1] and pos[i+1] == pos[i+2]:
            result += 1
        if pos[i] == pos[i+1] - 1 and pos[i+1] == pos[i+2]:
            result += 1
    for i in range(C-1):
        if pos[i] == pos[i+1]:
            result += 1
        if pos[i] == pos[i+1] + 2:
            result += 1

if P == 7:
    for i in range(C-2):
        if pos[i] == pos[i+1] and pos[i+1] == pos[i+2]:
            result += 1
        if pos[i] == pos[i+1] and pos[i+1] == pos[i+2] + 1:
            result += 1
    for i in range(C-1):
        if pos[i] == pos[i+1] - 2:
            result += 1
        if pos[i] == pos[i+1]:
            result += 1

print(result)


