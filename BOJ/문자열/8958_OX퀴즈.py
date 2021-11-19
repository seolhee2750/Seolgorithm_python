n = int(input())

for _ in range(n):
    now = input()
    check = False
    score = 0
    sum = 0
    for i in now:
        if i == 'O': score += 1; sum += score
        else: score = 0; check = False
    print(sum)
