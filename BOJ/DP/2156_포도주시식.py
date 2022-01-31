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