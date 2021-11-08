def solution(a, b):
    return sum(range(a, b+1)) if a < b else sum(range(b, a+1))

print(solution(3, 5))
print(solution(5, 3))