import sys

while True:
    now = sys.stdin.readline().strip()
    if int(now) == 0:
        break
    else:
        if now == now[::-1]:
            print("yes")
        else:
            print("no")