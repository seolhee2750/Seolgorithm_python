import sys
import heapq

n = int(sys.stdin.readline().strip())
heap_plus = []
heap_minus = []

for _ in range(n):
    now = int(sys.stdin.readline().strip())

    if now == 0:
        if heap_plus and heap_minus:
            if heap_plus[0] == heap_minus[0]:
                print(-heapq.heappop(heap_minus))
            else:
                if heap_plus[0] > heap_minus[0]:
                    print(-heapq.heappop(heap_minus))
                else:
                    print(heapq.heappop(heap_plus))
        else:
            if heap_plus:
                print(heapq.heappop(heap_plus))
            elif heap_minus:
                print(-heapq.heappop(heap_minus))
            else:
                print(0)
    else:
        if now > 0:
            heapq.heappush(heap_plus, now)
        else:
            heapq.heappush(heap_minus, -now)

