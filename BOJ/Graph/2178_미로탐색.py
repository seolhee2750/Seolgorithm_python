import sys

n, m = map(int, sys.stdin.readline().strip().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))
maze[0][0] = 0
queue = [(0, 0, 1)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = n*m

def bfs(queue):
    global answer
    idx = 0
    cnt = 0
    while idx < len(queue):
        x = queue[idx][0]
        y = queue[idx][1]
        cnt = queue[idx][2]
        idx += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or maze[nx][ny] == 0:
                continue
            if nx == n - 1 and ny == m - 1:
                answer = min(answer, cnt + 1)
                continue
            maze[nx][ny] = 0
            queue.append((nx, ny, cnt + 1))

bfs(queue)
print(answer)