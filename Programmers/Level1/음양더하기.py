def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(signs)):
        answer += absolutes[i] if signs[i] == True else - absolutes[i]
    return answer

print(solution([4,7,12], [True,False,True]))