def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += (A[i] * B[i])

    return answer

print(solution([1, 4, 2], [5, 4, 4]))

"""
[ 다른 사람 풀이 ]

def solution(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
"""