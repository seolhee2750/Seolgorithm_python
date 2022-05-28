import sys

n = int(sys.stdin.readline().strip())
times = []
for i in range(n):
    times.append(tuple(map(int, sys.stdin.readline().strip().split())))
times.sort(key=lambda x: (x[1], x[0]))
last = 0
cnt = 0

for i in times:
    if i[0] >= last:
        last = i[1]
        cnt += 1

print(cnt)