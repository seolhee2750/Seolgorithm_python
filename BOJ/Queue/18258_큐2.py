import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queue = deque()
for _ in range(n):
    now = sys.stdin.readline().strip()
    if now[0:2] == "pu":
        a, b = now.split()
        queue.append(int(b))
    elif now == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif now == "size":
        print(len(queue))
    elif now == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif now == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif now == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])