def solution(arr):
    tmp = -1
    answer = []
    for i in arr:
        if i == tmp: continue
        else: answer.append(i); tmp = i
    return answer

print(solution([1,1,3,3,0,1,1]))