def solution(arr, divisor):
    answer = list(filter(lambda x: (x % divisor == 0), arr))
    return sorted(answer) if len(answer) != 0 else [-1]

# 다른 사람 풀이
# 변형된 for문 형태, or 사용법 공부 필요!
"""
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]
"""