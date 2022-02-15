# BOJ #15649 N과 M (1) (백트래킹 입문예제)

n, m = map(int, input().split())
tmp = []

def dfs():
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(1, n+1):
        if i not in tmp:
            tmp.append(i)
            dfs()
            tmp.pop()

dfs()