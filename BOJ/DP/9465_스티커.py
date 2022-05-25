import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    if n == 1:
        a = int(sys.stdin.readline().strip())
        b = int(sys.stdin.readline().strip())
        print(max(a, b))
    else:
        sticker = []
        for _ in range(2):
            sticker.append(list(map(int, sys.stdin.readline().strip().split())))
        dp = [[0 for _ in range(n+1)] for _ in range(2)]
        dp[0][1], dp[1][1] = sticker[0][0], sticker[1][0]
        for i in range(2, n+1):
            for j in range(2):
                if j == 0:
                    dp[j][i] = max(dp[j+1][i-2:i]) + sticker[j][i-1]
                else:
                    dp[j][i] = max(dp[j-1][i-2:i]) + sticker[j][i-1]
        print(max(map(max, dp)))

"""
첫 번째 풀이

import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    if n == 1:
        a = int(sys.stdin.readline().strip())
        b = int(sys.stdin.readline().strip())
        print(max(a, b))
    else:
        sticker = []
        for _ in range(2):
            sticker.append(list(map(int, sys.stdin.readline().strip().split())))
        dp_a = [[0 for _ in range(n+1)] for _ in range(2)]
        dp_b = [[0 for _ in range(n+1)] for _ in range(2)]
        dp_a[0][1], dp_b[0][1] = sticker[0][0], sticker[0][0]
        dp_a[1][1], dp_b[1][1] = sticker[1][0], sticker[1][0]

        for i in range(2, n+1):
            for j in range(2):
                if j == 0:
                    dp_a[j][i] = max(dp_a[j+1][i-2], dp_b[j+1][i-2]) + sticker[j][i-1]
                    dp_b[j][i] = max(dp_a[j+1][i-1], dp_b[j+1][i-1]) + sticker[j][i-1]
                else:
                    dp_a[j][i] = max(dp_a[j - 1][i - 2], dp_b[j - 1][i - 2]) + sticker[j][i - 1]
                    dp_b[j][i] = max(dp_a[j - 1][i - 1], dp_b[j - 1][i - 1]) + sticker[j][i - 1]
        print(max(max(map(max, dp_a)), max(map(max, dp_b))))

=> 그 전에 포도주 시식이나 계단 오르기, RGB 거리 등등의 문제들과 비슷하게
1. 이 스티커를 선택했고 이전 대각선을 선택하지 않은 경우
2. 이 스티커를 선택했고 이전 대각선을 선택한 경우
이렇게 두 가지의 경우로 나누어서 연산을 해주었는데,
다 풀고 생각해보니 굳이 두 가지로 나눌 필요가 없는 문제였다,,!!
이 문제의 경우 현재 스티커를 선택하고 말고와 관계 없이 그 전 대각선을 선택하든 말든 상관이 없기 때문에
그냥 바로 이전 대각선과 그 전 대각선 중 더 큰 수를 골라서 누적해주면 된다.
"""