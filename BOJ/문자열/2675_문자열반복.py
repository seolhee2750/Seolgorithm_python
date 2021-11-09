n = int(input())
for _ in range(0, n):
    length, s = input().split()
    answer = ""
    for i in s:
        answer += i * int(length)
    print(answer)

