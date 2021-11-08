def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        if budget >= i:
            answer += 1
            budget -= i
        else: break
    return answer

print(solution([1,3,2,5,4], 9))

