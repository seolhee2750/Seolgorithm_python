# BOJ #15650 N과 M (2)

n, m = map(int, input().split())
tmp = []

def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(1, n+1):
        if len(tmp) == 0:
            tmp.append(i)
            dfs()
            tmp.pop()
        elif tmp[-1] < i:
            tmp.append(i)
            dfs()
            tmp.pop()

dfs()