import sys

t = int(sys.stdin.readline().strip())
dp = [[0 for _ in range(31)] for _ in range(31)]
for i in range(1, 31):
    for j in range(1, 31):
        if i == 1:
            dp[i][j] = j
        elif i == j:
            dp[i][j] = 1
        elif i < j:
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    print(dp[n][m])