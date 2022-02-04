def solution(s):
    num = '0123456789'
    answer = ''
    tmp = ''

    for i in range(len(s)):
        if s[i] == ' ':
            answer += tmp + ' '
            tmp = ''
        else:
            if tmp == '':
                if s[i] not in num:
                    tmp += s[i].upper()
                else:
                    tmp += s[i]
            else:
                tmp += s[i].lower()

    if tmp != '':
        answer += tmp
    return answer

print(solution("3people unFollowed me"))
print(solution("a b c"))
print(solution("33a, aab, 4"))