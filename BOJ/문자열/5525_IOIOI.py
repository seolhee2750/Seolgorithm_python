# BOJ #5525 IOIOI
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
idx = 0
count = 0
result = 0

while idx <= m-2:
    if s[idx : idx+3] == "IOI":
        idx += 2
        count += 1
        if count == n:
            result += 1
            count -= 1
    else:
        idx += 1
        count = 0

print(result)