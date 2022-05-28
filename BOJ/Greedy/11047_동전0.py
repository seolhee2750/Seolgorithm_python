import sys

n, k = map(int, sys.stdin.readline().strip().split())
coin = []
for i in range(n):
    a = int(sys.stdin.readline().strip())
    if a <= k:
        coin.append(a)
coin = coin[::-1]
cnt = 0

for i in coin:
    if k >= i:
        cnt += int(k / i)
        k = int(k % i)
    if k == 0:
        print(cnt)
        break