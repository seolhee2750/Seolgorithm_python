n, k = map(int, input().split())
if n == k:
    print(0)
elif max(n, k)-min(n, k) == 1:
    print(1)
else:
    check = [0 for i in range(0, 100001)]
    check[k] = -1
    queue = [(n, 0)]
    idx = 0
    find = False

    def case(i, x):
        if i == 0:
            return x - 1
        elif i == 1:
            return x + 1
        else:
            return 2 * x

    while True:
        (x, cnt) = queue[idx]
        idx += 1
        for i in range(3):
            nx = case(i, x)
            if nx < 0 or nx >= 100001 or check[nx] == 1:
                continue
            if check[nx] == -1:
                find = True
                break
            queue.append((nx, cnt+1))
            check[nx] = 1
        if find:
            print(cnt+1)
            break