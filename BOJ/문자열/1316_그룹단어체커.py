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