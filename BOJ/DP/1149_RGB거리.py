"""
집을 빨, 초, 파 셋 중 하나로 칠하는데, 같은 색이 연속될 수 없음
=> '최소'값의 후보는 총 세 가지 경우가 있음
(1) 빨간색으로 칠할 경우
(2) 초록색으로 칠할 경우
(3) 파란색으로 칠할 경우

대표로 (1)번을 예로 들자면
이번 집에는 빨간색을 칠할 것으로 가정하는 것이 (1)번 배열이며,
빨간색으로 칠한다는 것은 이전 집은 초록 혹은 파랑으로 칠했다는 의미가 되므로
우리는 최소 비용을 구해야하기 떄문에 이전 집의 초록, 파랑 중 더 저렴한 것을 골라 더해주면 됨
"""

n = int(input())

r, g, b = map(int, input().split())
red = [r]
green = [g]
blue = [b]

for i in range(1, n):
    r, g, b = map(int, input().split())
    red.append(r + min(green[i-1], blue[i-1]))
    green.append(g + min(red[i-1], blue[i-1]))
    blue.append(b + min(red[i-1], green[i-1]))

print(min(red[-1], blue[-1], green[-1]))