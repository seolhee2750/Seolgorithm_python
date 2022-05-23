sums = input().split("-")
for i in range(len(sums)):
    tmp = list(map(int, sums[i].split("+")))
    sums[i] = sum(tmp)

answer = sums[0]
if len(sums) == 1:
    print(answer)
else:
    for i in range(1, len(sums)):
        answer -= sums[i]
    print(answer)