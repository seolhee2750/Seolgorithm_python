t = int(input())

for _ in range(t):
    now = input()
    tmp = 0
    check = True

    for i in now:
        if i == "(":
            tmp += 1
        else:
            tmp -= 1
            if tmp == -1:
                check = False
        if not check:
            break

    if tmp == 0:
        print("YES")
    else:
        print("NO")