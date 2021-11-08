def solution(n, lost, reserve):
    students = [1] * n
    for i in lost: students[i-1] -= 1
    for i in reserve: students[i-1] += 1
    for i in range(0, n):
        if students[i] == 2:
            if i == 0:
                if ((students[i] == 2) & (students[i+1])) == 0:
                    students[i] = 1; students[i+1] = 1
            elif i == n-1:
                if ((students[i] == 2) & (students[i-1])) == 0:
                    students[i] = 1; students[i-1] = 1
            else:
                if students[i-1] == 0: students[i] = 1; students[i-1] = 1
                elif students[i+1] == 0: students[i] = 1; students[i+1] = 1
    return n - students.count(0)

print(solution(5, [2, 4], [3]))