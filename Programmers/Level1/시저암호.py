def solution(s, n):
    alphabet1 = list("abcdefghijklmnopqrstuvwxyz")
    alphabet2 = list("abcdefghijklmnopqrstuvwxyz".upper())
    answer = list(s)
    for i in range(0, len(answer)):
        if answer[i] == " ":
            continue
        elif answer[i] in alphabet1:
            answer[i] = alphabet1[(alphabet1.index(answer[i]) + n) % 26]
        else:
            answer[i] = alphabet2[(alphabet2.index(answer[i]) + n) % 26]
    return "".join(answer)

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))