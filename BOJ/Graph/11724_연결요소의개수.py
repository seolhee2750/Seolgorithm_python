# BOJ #11724 연결 요소의 개수

# N이 10000까지 입력될 수 있으므로 아래와 같이 바꿔주어야 함
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
connected = [[] for _ in range(n)]
visited = [0] * n
count = 0

for i in range(m):
    a, b = map(int, input().split())
    connected[a-1].append(b-1)
    connected[b-1].append(a-1)

def dfs(x):
    if visited[x] > 0: return
    visited[x] = count

    for i in connected[x]: dfs(i)

for i in range(n):
    if visited[i] == 0 and len(connected[i]) > 0:
        count += 1
        dfs(i)

# 아무 것도 이어지지 않은 혼자 남은 점 또한 하나의 연결 요소가 됨
for i in visited:
    if i == 0: count += 1

print(count)

"""
두 번째 풀이

import sys

n, m = map(int, sys.stdin.readline().strip().split())
connect = [[] for _ in range(n+1)]
check = [0 for _ in range(n+1)]
queue = []
cnt = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    connect[u].append(v)
    connect[v].append(u)

def bfs(queue):
    idx = 0
    while idx < len(queue):
        x = queue[idx]
        idx += 1
        check[x] = cnt
        for i in connect[x]:
            if check[i] > 0:
                continue
            else:
                check[i] = cnt
                if len(connect[i]) == 0:
                    continue
                else:
                    queue.append(i)

for i in range(1, n+1):
    if check[i] > 0:
        continue
    cnt += 1
    check[i] = cnt
    if len(connect[i]) == 0:
        continue
    for j in range(len(connect[i])):
        queue.append(connect[i][j])
    bfs(queue)
    queue = []

print(max(check))

=> bfs로 풀이하였음
"""