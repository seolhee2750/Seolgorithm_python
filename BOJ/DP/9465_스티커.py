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