def solution(strings, n):
    return sorted(sorted(strings), key = lambda x: x[n])

# 다른 사람 풀이
# strings의 요소마다, n번째 글자를 맨 앞에 붙인 후 정렬하고, 다시 맨 앞글자만 뺀 나머지를 모두 answer에 추가하여 리턴!
"""
def solution(strings, n):
    answer = []
    for i in range(len(strings)): strings[i] += strings[i][n]
    strings.sort()
    for i in range(len(strings)): answer.append(strings[i][1:])
    return answer
"""
