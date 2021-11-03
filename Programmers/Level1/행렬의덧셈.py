def solution(arr1, arr2):
    answer = arr1
    for i in range(0, len(arr2)) :
        for j in range(0, len(arr2[i])) :
            answer[i][j] += arr2[i][j]
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))