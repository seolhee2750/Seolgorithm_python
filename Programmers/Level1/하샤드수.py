def solution(x):
    num = str(x)
    result = 0
    for i in num:
        result += int(i)
    if x % result == 0:
        return True
    else:
        return False

print(solution(19))
print(solution(20))