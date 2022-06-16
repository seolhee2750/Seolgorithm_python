import sys
import heapq

n = int(sys.stdin.readline().strip())
heap = []
for _ in range(n):
    now = int(sys.stdin.readline().strip())
    if now == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -now)