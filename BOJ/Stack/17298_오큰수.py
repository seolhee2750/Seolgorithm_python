import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
arr = []
answer = ["-1" for _ in range(n)]

for i in range(n):
    while True:
        if len(arr) == 0 or arr[-1][0] >= a[i]:
            arr.append((a[i], i))
            break
        else:
            answer[arr.pop()[1]] = str(a[i])

print(" ".join(answer))
