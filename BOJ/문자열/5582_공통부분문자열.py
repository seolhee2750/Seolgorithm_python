import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
cnt = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            cnt[i+1][j+1] = cnt[i][j] + 1

print(max(map(max, cnt)))

"""
import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
answer = 0

for i in range(len(a)):
    for j in range(0, len(b)):
        if a[i] == b[j]:
            idx = 0
            while i+idx < len(a) and j+idx < len(b):
                if a[i+idx] == b[j+idx]:
                    idx += 1
                else:
                    break
            if answer < idx:
                answer = idx

print(answer)
"""

"""
처음엔 dp 사용하지 않고 그냥 비교해주었다가 시간초과났음
따라서 dp로 풀이했는데, 그래도 계속 시간초과나서 pypy로 제출함
"""
