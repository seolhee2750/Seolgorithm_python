n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1:
            dp[i][j] = p[i] * j
        elif i > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i][j-i] + p[i], dp[i-1][j-i] + p[i], dp[i-1][j])

print(dp[-1][-1])