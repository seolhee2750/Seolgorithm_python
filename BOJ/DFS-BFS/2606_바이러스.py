# BOJ #2606 바이러스

n = int(input())
c = int(input())
network = [[] for _ in range(n)]
queue = []
visited = [False] * n
count = 0

for _ in range(c):
    a, b = map(int, input().split())
    network[a-1].append(b-1)
    network[b-1].append(a-1)

def dfs(x):
    if visited[x]: return
    visited[x] = True

    for i in range(len(network[x])):
        dfs(network[x][i])

dfs(0)
for i in visited:
    if i: count += 1
print(count-1)
