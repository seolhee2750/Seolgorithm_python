def solution(s):
    if (len(s) == 4) | (len(s) == 6):
        try:
            int(s)
            return True
        except ValueError:
            return False
    else: return False

print(solution("a123"))
print(solution("1234"))

# 다른 사람 풀이 => isdigit() 함수!!
"""
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
"""