def solution(phone_number):
    answer = ""
    num = len(phone_number)
    for i in range(0, num):
        if i >= (num - 4):
            answer += str(phone_number[i])
        else:
            answer += "*"
    return answer

print(solution("01033334444"))