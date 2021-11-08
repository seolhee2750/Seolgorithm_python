def digitConversion(n, divisor):
    answer = ''
    while n > 0:
        n, mod = divmod(n, divisor)
        answer += str(mod)
    return answer

def solution(n):
    return int(digitConversion(n, 3), 3)

print(solution(45))

# 다른 사람 풀이
# 새로운(?) while 사용법,,! 어차피 n이 0이 되면 False와 같으므로, 굳이 while n > 0: 이렇게 안해도 됨
"""
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
"""