n = int(input())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
count = 0

for _ in range(0, n):
    s = input()
    tmp = ''
    answer = True
    check = [0] * 26
    for i in s:
        if tmp != i:
            if check[alphabet.index(i)] == 1:
                answer = False
                break
            else:
                check[alphabet.index(i)] = 1
                tmp = i
    if answer == True: count += 1

print(count)

"""
두 번째 풀이

n = int(input())
result = 0

for i in range(n):
    s = input()
    check = []
    go = True

    for i in s:
        if i in check:
            if check.index(i) != len(check)-1:
                go = False
        else:
            check.append(i)
        if not go:
            break

    if go:
        result += 1

print(result)
"""