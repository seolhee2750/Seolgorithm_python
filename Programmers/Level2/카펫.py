def solution(brown, yellow):
    answer = []

    for i in range(3, brown):
        if (i - 2) * ((brown - (i * 2)) / 2) == yellow:
            answer = [(brown - (i * 2)) / 2 + 2, i]
            break

    return answer

print(solution(10, 2))
print(solution(24, 24))