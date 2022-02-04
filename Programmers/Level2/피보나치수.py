def solution(n):
    a = 0  # F(0)
    b = 1  # F(1)
    idx = 1

    while idx < n:
        tmp = (a + b) % 1234567
        a = b
        b = tmp
        idx += 1

    return b

print(solution(3))
print(solution(5))