import sys
import math

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
INF = math.inf
table = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    table[a-1][b-1] = min(table[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                table[i][j] = 0
            else:
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])

for i in range(n):
    for j in range(n):
        if table[i][j] == INF:
            table[i][j] = 0

print('\n'.join(' '.join(map(str, i)) for i in table))