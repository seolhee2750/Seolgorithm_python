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