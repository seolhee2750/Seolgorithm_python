def solution(a, b):
    day = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day[(sum(month[0:a-1]) + b) % 7 - 1]

print(solution(5, 24))