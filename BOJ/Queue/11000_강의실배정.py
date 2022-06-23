import sys
import heapq

n = int(sys.stdin.readline().strip())
times = [] # 입력되는 강의 시간들을 튜플 형태로 저장
rooms = [] # 각 원소가 하나의 강의실을 뜻하는 배열
for _ in range(n):
    (start, end) = map(int, sys.stdin.readline().strip().split())
    times.append((start, end))
times.sort(key=lambda x: (x[0], x[1])) # 시작 시간을 기준으로 오름차순 정렬, 시작시간이 같을 경우 종료 시간 기준 오름차순 정렬

for i in times:
    (start, end) = i
    if rooms and rooms[0] <= start:
        heapq.heappop(rooms) # rooms의 최솟값 pop
    heapq.heappush(rooms, end) # rooms에 현재 강의의 종료 시간 push

print(len(rooms))