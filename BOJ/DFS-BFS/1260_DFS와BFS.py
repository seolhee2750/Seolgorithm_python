import sys
sys.setrecursionlimit(10 ** 4)

n, m, v = map(int, sys.stdin.readline().strip().split())
line = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    line[a].append(b)
    line[b].append(a)
for i in line:
    i.sort()

check_dfs = [False for _ in range(n+1)]
answer_dfs = []

def dfs(x):
    if not check_dfs[x]:
        check_dfs[x] = True
        answer_dfs.append(x)
        if len(line[x]) != 0:
            for t in range(len(line[x])):
                dfs(line[x][t])
    else:
        return

check_bfs = [False for _ in range(n+1)]
answer_bfs = []

def bfs(queue):
    while len(queue) > 0:
        tmp = []
        for i in queue:
            answer_bfs.append(i)
            check_bfs[i] = True
            for j in line[i]:
                if not check_bfs[j]:
                    check_bfs[j] = True
                    tmp.append(j)
        queue = tmp

dfs(v)
bfs([v])
print(" ".join(map(str, answer_dfs)))
print(" ".join(map(str, answer_bfs)))
