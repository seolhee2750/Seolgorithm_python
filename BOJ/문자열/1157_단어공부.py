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