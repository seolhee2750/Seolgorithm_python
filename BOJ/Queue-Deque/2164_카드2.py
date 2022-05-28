import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queue = deque(i+1 for i in range(n))
idx = 0

while len(queue) > 1:
    if idx % 2 == 0:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    idx += 1

print(queue[0])