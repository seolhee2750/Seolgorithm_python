# BOJ #4963 섬의 개수
import sys
sys.setrecursionlimit(10000)

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    space = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    dx = [0, 0, -1, 1, -1, 1, -1, 1]
    dy = [-1, 1, 0, 0, -1, 1, 1, -1]
    count = 0

    def dfs(x, y):
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w or space[nx][ny] == 0: continue

            space[nx][ny] = 0
            dfs(nx, ny)

    for i in range(h):
        for j in range(w):
            if space[i][j] == 1:
                count += 1
                space[i][j] = 0
                dfs(i, j)

    print(count)