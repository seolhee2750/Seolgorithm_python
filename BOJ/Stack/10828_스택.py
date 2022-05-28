import sys

n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    now = sys.stdin.readline().strip()
    if now[0:2] == "pu":
        a, b = now.split()
        arr.append(int(b))
    elif now == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(-1))
    elif now == "size":
        print(len(arr))
    elif now == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif now == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])