def solution(numbers):
    answer = 0
    for i in range(0, 10):
        if i not in numbers: answer += i
    return answer

print(solution([1,2,3,4,6,7,8,0]))

# 다른 사람 풀이
"""
def solution(numbers):
    return 45 - sum(numbers)
"""