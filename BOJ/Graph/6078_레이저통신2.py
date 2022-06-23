import sys
import math

w, h = map(int, sys.stdin.readline().strip().split())
table = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
points = []

for i in range(h):
    now = list(sys.stdin.readline().strip())
    for j in range(w):
        if now[j] == 'C':
            points.append((i, j))
    table.append(now)

def bfs(x, y):
    visited = [[[math.inf] * 4 for _ in range(w)] for _ in range(h)]
    queue = []
    idx = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= h or ny >= w or table[nx][ny] == '*':
            continue
        queue.append((nx, ny, i))
        visited[nx][ny][i] = 0

    while idx < len(queue):
        (x, y, direct) = queue[idx]
        idx += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or table[nx][ny] == '*':
                continue

            cnt = visited[x][y][direct]
            if (direct <= 1 and i > 1) or (direct > 1 and i <= 1):
                cnt += 1
            if visited[nx][ny][i] == -1:
                visited[nx][ny][i] = cnt
                queue.append((nx, ny, i))
            elif visited[nx][ny][i] > cnt:
                visited[nx][ny][i] = cnt
                queue.append((nx, ny, i))

    return min(visited[points[1][0]][points[1][1]])

print(bfs(points[0][0], points[0][1]))