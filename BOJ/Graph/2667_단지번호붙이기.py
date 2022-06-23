import sys

n = int(sys.stdin.readline().strip())
table = []
for _ in range(n):
    table.append(list(map(int, list(sys.stdin.readline().strip()))))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = []
tmp = 0

def dfs(x, y, cnt):
    global tmp
    if x < 0 or y < 0 or x >= n or y >= n or table[x][y] == 0:
        return

    table[x][y] = 0
    tmp = max(tmp, cnt)

    for i in range(4):
        dfs(x+dx[i], y+dy[i], tmp+1)

for i in range(n):
    for j in range(n):
        if table[i][j] == 1:
            dfs(i, j, 1)
            answer.append(tmp)
            tmp = 0

print(len(answer))
print("\n".join(list(map(str, sorted(answer)))))