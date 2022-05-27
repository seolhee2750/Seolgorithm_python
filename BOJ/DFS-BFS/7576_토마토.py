# BOJ #7576 토마토
import sys, copy
m, n = map(int, sys.stdin.readline().split())
storage = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
countCheck = copy.deepcopy(storage)
result = 0
zero = False

def bfs(count):
    index = 0
    while len(queue) > index:
        x, y, n_count = queue[index][0], queue[index][1], queue[index][2]
        index += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if storage[nx][ny] == 0:
                storage[nx][ny] = 1
                countCheck[nx][ny] = n_count+1
                queue.append((nx, ny, n_count+1))

for i in range(n):
    for j in range(m):
        if storage[i][j] == 1:
            queue.append((i, j, 0))
        if storage[i][j] == 0:
            zero = True

if zero == False:
    print(0)
else:
    bfs(0)
    for i in range(n):
        if 0 in storage[i]:
            result = -1
            break
        result = max(result, max(countCheck[i]))

    print(result)

"""
두 번째 풀이

import sys

m, n = map(int, sys.stdin.readline().strip().split())
table = []
queue = []
zero = 0

for i in range(n):
    table.append(list(map(int, sys.stdin.readline().strip().split())))
    for j in range(m):
        if table[i][j] == 1:
            queue.append((i, j, 0))
        elif table[i][j] == 0:
            zero += 1

if zero == 0:
    print(0)
else:
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    idx = 0

    while idx < len(queue):
        (x, y, cnt) = queue[idx]
        idx += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if table[nx][ny] == 0:
                queue.append((nx, ny, cnt + 1))
                zero -= 1
                table[nx][ny] = 1

    if zero > 0:
        print(-1)
    else:
        print(queue[-1][-1])
"""