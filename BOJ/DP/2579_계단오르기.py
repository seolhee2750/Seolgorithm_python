# BOJ #2579 계단 오르기
import sys

n = int(sys.stdin.readline())
a = [0]*n # 현재 계단 밟고, 직전 계단 밟았다고 할 때
b = [0]*n # 현재 계단 밟고, 직전 계단 밟지 않았다고 할 때

for i in range(n):
    now = int(sys.stdin.readline())

    if i == 0:
        a[i] = now
        b[i] = now
    elif i == 1:
        a[i] = now + b[i-1]
        b[i] = now
    else:
        a[i] = now + b[i - 1]
        b[i] = now + max(a[i - 2], b[i - 2])

print(max(a[-1], b[-1]))