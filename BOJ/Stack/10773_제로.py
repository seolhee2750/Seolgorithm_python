import sys

k = int(sys.stdin.readline().strip())
arr = []
for i in range(k):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))