# BOJ #2156 포도주 시식
import sys

n = int(sys.stdin.readline())
wine = []
for _ in range(n):
    wine.append(int(sys.stdin.readline()))

if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0]+wine[1])
elif n == 3:
    print(max(wine[0]+wine[2], wine[1]+wine[2], max(wine[0]+wine[1], wine[0]+wine[2], wine[1]+wine[2])))
else:
    sums = [wine[0], wine[0]+wine[1]]
    sums.append(max(wine[0]+wine[2], wine[1]+wine[2], sums[1]))
    for i in range(3, n):
        sums.append(max(wine[i]+sums[i-2], wine[i]+wine[i-1]+sums[i-3], sums[i-1]))
    print(max(sums))

"""
두 번째 풀이

import sys

n = int(sys.stdin.readline().strip())
if n == 1:
    print(int(sys.stdin.readline().strip()))
else:
    a = [0] # 현재 포도주를 마시고, 이전 포도주는 마시지 않을 때
    b = [0] # 현재 포도주를 마시고, 이전 포도주도 마실 때
    now = int(sys.stdin.readline().strip())
    a.append(now)
    b.append(now)
    for i in range(2, n+1):
        now = int(sys.stdin.readline().strip())
        a.append(max(max(a[:i-1]), max(b[:i-1])) + now)
        b.append(a[i-1] + now)
    print(max(max(a), max(b)))
    
=> 풀이는 더 간단하지만, 효율면에서는 첫 번째 풀이가 더 좋음
"""