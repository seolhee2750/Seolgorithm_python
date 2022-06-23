import sys
import math

w, h = map(int, sys.stdin.readline().strip().split())
table = []
visited = [[math.inf for _ in range(w)] for _ in range(h)]
queue = []
dx = [0, 0, -1, 1]  # 수직 이동
dy = [-1, 1, 0, 0]  # 수평 이동
answer = math.inf

for i in range(h):
    now = list(sys.stdin.readline().strip())
    if 'C' in now and not queue:
        # bfs 함수 돌리기 위한 시작점으로 넣어줌 (행, 열, 최소 누적 거울 개수, 수직 이동 여부)
        queue.append((i, now.index('C'), 0, False))
        queue.append((i, now.index('C'), 0, True))
        visited[i][now.index('C')] = 0
    table.append(now)

print(queue)

def bfs():
    global answer
    global visited
    idx = 0

    while idx < len(queue):
        (x, y, mirror, vertical) = queue[idx]
        idx += 1

        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]

            if nx < 0 or ny < 0 or nx >= h or ny >= w or table[nx][ny] == '*' or visited[nx][ny] <= mirror:
                continue

            if table[nx][ny] == 'C':
                if (a <= 1 and vertical) or (a > 1 and not vertical):
                    answer = min(answer, mirror + 1)
                else:
                    answer = min(answer, mirror)
                continue

            mirror_tmp = mirror
            vertical_tmp = vertical

            # 수평 이동할 것이나, 그 전까지는 수직으로 이동해온 경우 (방향 바꿈, 거울 추가)
            if a <= 1 and vertical:
                mirror_tmp += 1
                vertical_tmp = False
            # 수직 이동할 것이나, 그 전까지는 수평으로 이동해온 경우 (방향 바꿈, 거울 추가)
            elif a > 1 and not vertical:
                mirror_tmp += 1
                vertical_tmp = True

            queue.append((nx, ny, mirror_tmp, vertical_tmp))
            visited[nx][ny] = min(visited[nx][ny], mirror_tmp)

bfs()
print(answer)
print('\n'.join(' '.join(map(str, i)) for i in visited))