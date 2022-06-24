import sys
import math

w, h = map(int, sys.stdin.readline().strip().split())
table = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
points = [] # 'C'의 위치 (처음 입력받는 위치를 시작점, 나중에 입력받는 위치를 도착점으로 설정함)

for i in range(h):
    now = list(sys.stdin.readline().strip())
    for j in range(w):
        if now[j] == 'C':
            points.append((i, j))
    table.append(now)

def bfs(x, y):
    visited = [[[math.inf] * 4 for _ in range(w)] for _ in range(h)] # 방문 체크
    queue = [] # 탐색할 위치의 정보 (행, 열, 방향)
    idx = 0

    # 본격적으로 탐색 전 queue에 가장 먼저 탐색을 시작할 위치들 추가
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= h or ny >= w or table[nx][ny] == '*':
            continue
        queue.append((nx, ny, i)) # i값을 통해 그 전까지 어떤 방향으로 움직였는지를 알 수 있게 함
        visited[nx][ny][i] = 0

    while idx < len(queue):
        (x, y, direct) = queue[idx]
        idx += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or table[nx][ny] == '*':
                continue

            cnt = visited[x][y][direct] # 이전 자리의 방향 값을 통해 거울을 추가해야 하는지 정하기 위함
            if (direct <= 1 and i > 1) or (direct > 1 and i <= 1):
                cnt += 1

            # 방문한적 없는 자리일 경우, 거울 개수 그대로 저장 / 방문한적 있을 경우 더 작은 값으로 갱신
            if visited[nx][ny][i] == -1:
                visited[nx][ny][i] = cnt
                queue.append((nx, ny, i))
            elif visited[nx][ny][i] > cnt:
                visited[nx][ny][i] = cnt
                queue.append((nx, ny, i))

    # 도착 지점에 저장된 거울 개수 중 가장 작은 수 반환
    return min(visited[points[1][0]][points[1][1]])

# 시작 지점 좌표 넣어서 bfs 함수 호출
print(bfs(points[0][0], points[0][1]))