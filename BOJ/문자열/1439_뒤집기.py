s = input()
tmp = s[0]
cnt = 0
for i in range(1, len(s)):
    if s[i] != tmp:
        tmp = s[i]
        cnt += 1

if cnt <= 1:
    print(cnt)
else:
    if cnt % 2 == 0:
        print(int(cnt/2))
    else:
        print(int(cnt/2 + 1))