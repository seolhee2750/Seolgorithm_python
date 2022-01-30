import copy

n, m = map(int, input().split())
space = [] # 문제에서 주어진 지도
virusSpace = [] # 바이러스의 위치

""" 입력 """
for i in range(n):
    space.append(list(map(lambda x: int(x), input().split())))
    for j in range(m):
        if space[i][j] == 2:
            virusSpace.append((i, j))

check = copy.deepcopy(space)
result = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

""" 바이러스 전파 """
def dfs(x, y, check):
    if check[x][y] == 2:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue

            if check[nx][ny] == 0:
                check[nx][ny] = 2
                dfs(nx, ny, check)

""" 벽 세우는 모든 경우의 수 탐색 """
def makeWall(start, count):
    global result
    safe_count = 0

    if count == 3:
        check = copy.deepcopy(space)
        for i in virusSpace:
            dfs(i[0], i[1], check)

        for i in range(n):
            safe_count += check[i].count(0)
        result = max(result, safe_count)
        return

    else:
        for i in range(start, n*m):
            x = i // m
            y = i % m
            if space[x][y] == 0:
                space[x][y] = 1
                makeWall(i, count+1)
                space[x][y] = 0

makeWall(0, 0)
print(result)