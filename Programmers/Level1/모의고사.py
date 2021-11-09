def solution(answers):
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]

    for i in range(0, len(answers)):
        if answers[i] == stu1[i % 5]: count[0] += 1
        if answers[i] == stu2[i % 8]: count[1] += 1
        if answers[i] == stu3[i % 10]: count[2] += 1

    maxCount = max(count)
    for i in range(0, 3): count[i] = i+1 if count[i] == maxCount else 0

    return list(filter(lambda x: x != 0, count))

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))