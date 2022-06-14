import sys
import heapq

n = int(sys.stdin.readline().strip())
left = []
right = []

for _ in range(n):
    now = int(sys.stdin.readline().strip())

    if len(left) == len(right):
        heapq.heappush(left, -now)
    else:
        heapq.heappush(right, now)

    if right and right[0] < -left[0]:
        leftNum = heapq.heappop(left)
        rightNum = heapq.heappop(right)

        heapq.heappush(left, -rightNum)
        heapq.heappush(right, -leftNum)

    print(-left[0])