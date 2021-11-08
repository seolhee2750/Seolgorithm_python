def solution(s):
    count_p = 0
    count_y = 0
    for i in s:
        if i in "pP": count_p += 1
        elif i in "yY": count_y += 1
    return True if count_p == count_y else False

print(solution("pPoooyY"))

# 다른 사람 풀이
# 그냥 다 소문자로 만들어서 p랑 y 찾아주기 !
"""
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
"""