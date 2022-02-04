def solution(s):
    num_s = list(map(int, s.split()))
    return str(min(num_s)) + " " + str(max(num_s))

print(solution("1 2 3 4"))
print(solution("-1 -1"))