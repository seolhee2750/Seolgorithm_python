# 플로이드 워셜 문제 풀이

import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline().strip())
table = []
for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().strip().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if table[i][k] and table[k][j]:
                table[i][j] = 1

print('\n'.join(' '.join(map(str, i)) for i in table))

"""
BFS 문제 풀이

import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline().strip())
table = []
for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().strip().split())))
result = table

def bfs(queue, find, checkList):
    idx = 0
    check = False

    while idx < len(queue):
        now = queue[idx]
        idx += 1

        if 1 not in table[now]:
            continue
        else:
            for x in range(n):
                if table[now][x] == 1 and checkList[now][x] is False:
                    checkList[now][x] = True
                    if x == find:
                        check = True
                        break
                    else:
                        queue.append(x)
                if check:
                    break

        if check:
            break

    if check:
        return 1
    else:
        return 0

for i in range(n):
    for j in range(n):
        if result[i][j] == 1:
            continue
        else:
            checkList = [[False for _ in range(n)] for _ in range(n)]
            checkList[i][j] = True
            result[i][j] = bfs([i], j, checkList)

print('\n'.join(' '.join(map(str, i)) for i in result))
"""