import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())
queue = deque(i+1 for i in range(n))
tmp = deque()
cnt = 0
idx = 1
answer = []

while cnt < n:
    if len(queue) == 0:
        queue += tmp
        tmp.clear()
        continue
    if idx % k == 0:
        answer.append(str(queue.popleft()))
        cnt += 1
        idx += 1
        continue
    if idx % k != 0:
        tmp.append(queue.popleft())
        idx += 1
        continue

print("<" + ", ".join(answer) + ">")