s = input().upper()
if len(s) == 1: print(s)
else:
    d = dict()
    for i in s:
        if d.get(i) == None: d[i] = 1
        else: d[i] += 1
    d = sorted(d.items(), key=lambda x: x[1])
    if d[len(d) - 1][1] == d[len(d) - 2][1]: print("?")
    else: print(d[len(d) - 1][0])

# 딕셔너리는 정렬 시 [튜플] 형태로 반환함

"""
두 번째 풀이

s = input().upper()
a = list("abcdefghijklmnopqrstuvwxyz".upper())
check = [0] * 26
for i in s:
    check[a.index(i)] += 1

m = check.index(max(check))
tmp = 25
for i in reversed(range(0, len(check))):
    if check[i] > check[tmp]:
        tmp = i

if m == tmp:
    print(a[m])
else:
    print("?")
"""