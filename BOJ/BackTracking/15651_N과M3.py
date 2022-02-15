# BOJ #15651 N과 M (3)

n, m = map(int, input().split())
tmp = []
result = []

def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(1, n+1):
        tmp.append(i)
        dfs()
        tmp.pop()

dfs()