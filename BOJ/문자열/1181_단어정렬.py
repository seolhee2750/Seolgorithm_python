# BOJ #1181 단어 정렬
import sys

n = int(sys.stdin.readline())
result = []

for _ in range(n):
    now = sys.stdin.readline().strip()
    result.append((len(now), now))

result = list(set(result))
result.sort()

for i in range(len(result)):
    print(result[i][1])
