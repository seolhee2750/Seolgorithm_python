import sys

n, k = map(int, sys.stdin.readline().strip().split())
coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline().strip()))
dp = [0 for _ in range(k+1)]
dp[0] = 1

for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i - c]

print(dp[-1])