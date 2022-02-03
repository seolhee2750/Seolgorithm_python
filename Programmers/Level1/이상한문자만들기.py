def solution(s):
    answer = ""
    count = 0
    for i in s:
        if i == " ":
            count = 0
            answer += i
        else:
            if count % 2 == 0: answer += i.upper()
            else: answer += i.lower()
            count += 1
    return answer

print(solution("try hello world"))
print(solution("Apple is Delicious"))

"""
[ 두 번째 문제 풀이 ]

def solution(s):
    answer = ''
    idx = 0
    check = 0
    
    while len(answer) < len(s):
        if s[idx] == ' ': 
            answer += ' '
            check = 0
        else:
            if check % 2 == 0: answer += s[idx].upper()
            else: answer += s[idx].lower()
            check += 1
        idx += 1
    
    return answer
"""