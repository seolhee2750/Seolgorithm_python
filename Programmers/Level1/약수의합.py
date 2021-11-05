def solution(n):
    if n <= 1: return n
    else:
        answer = set()
        for i in range(1, int(n**(1/2))+1):
            if n % i == 0:
                answer.add(n / i)
                answer.add(i)
        return sum(answer)

print(solution(12))