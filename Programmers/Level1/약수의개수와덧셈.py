def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if i == 1: answer -= i
        elif i <= 3: answer += i
        else:
            tmp = set()
            for j in range(1, int(i**(1/2))+1):
                if i % j == 0:
                    tmp.add(j)
                    tmp.add(i/j)
            if len(tmp) % 2 == 0: answer += i
            else: answer -= i
    return answer

print(solution(13, 17))