a, b = map(int, input().split())
c = int(input())
t = b + c

if t >= 60:
    print(int((a + (t / 60)) % 24), t % 60)
else:
    print(a, t)