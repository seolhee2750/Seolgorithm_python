def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0]; j = c[1]; k = c[2]
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

"""
[ 두 번째 풀이 ]

def solution(array, commands):
    answer = []
    
    for c in commands:
        i, j, k = c[0], c[1], c[2]
        answer.append(sorted(array[i-1:j])[k-1])

    return answer
"""