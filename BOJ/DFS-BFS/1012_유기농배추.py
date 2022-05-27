# BOJ #1012 유기농 배추
"""
파이썬 논리 연산자는 or, and 같이 영어로,, 쓰자,,!!
"""

t = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = []

for _ in range(t):
    m, n, k = map(int, input().split())  # 가로길이, 세로길이, 배추 개수
    space = [[0] * m for _ in range(n)]  # 배추밭
    count = 0

    for _ in range(k):
        y, x = map(int, input().split())
        space[x][y] = 1

    def bfs():
        index = 0

        while len(queue) > index:
            x = queue[index][0]
            y = queue[index][1]
            index += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m or space[nx][ny] == 0: continue

                space[nx][ny] = 0
                queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if space[i][j] == 1:
                queue.append((i, j))
                space[i][j] = 0
                count += 1
                bfs()
                queue = []

    print(count)

"""
두 번째 풀이

import sys
sys.setrecursionlimit(10 ** 4)

t = int(sys.stdin.readline().strip())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    table = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        table[y][x] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    cnt = 0

    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= m or table[x][y] != 1:
            return
        table[x][y] = 0
        for i in range(4):
            dfs(x+dx[i], y+dy[i])

    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)
    
=> 재귀 dfs 이용하여 풀이하였음
재귀 깊이를 늘려주어야 함
"""