def solution(num):
    count = 0
    while True:
        if (num == 1) | (count == 500): break
        elif num % 2 == 0: num /= 2
        else: num = (num * 3) + 1
        count += 1
    return -1 if count == 500 else count

print(solution(6))

# 파이썬은 비트 연산자 사용 시 (num == 1) | (count == 500) 이렇게 괄호를 잘 해줘야 함..**