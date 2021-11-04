def solution(n):
    n = list(str(n))
    n.reverse()
    return list(map(int, n))

print(solution(12345))

# reverse도 sort와 마찬가지로, 값을 반환하지 않으며 딱 reverse만 하게 따로 빼서 사용해야 함