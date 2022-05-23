import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    x = sys.stdin.readline().strip()
    lst = list(x[1:len(x)-1].split(","))

    rev = False
    front = 0
    back = 0
    error = False

    for i in p:
        if i == "R":
            if rev:
                rev = False
            else:
                rev = True
        else:
            if rev:
                back += 1
            else:
                front += 1
            if front + back > n:
                error = True
        if error:
            break

    if error:
        print("error")
    else:
        if rev:
            print("[" + ",".join(lst[::-1][back:(n-front)]) + "]")
        else:
            print("[" + ",".join(lst[front:(n-back)]) + "]")
