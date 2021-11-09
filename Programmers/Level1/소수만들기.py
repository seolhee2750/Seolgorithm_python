def solution(nums):
    case = []
    answer = 0

    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                case.append(nums[i] + nums[j] + nums[k])

    for i in case:
        check = True
        for j in range(2, int(i ** (1 / 2)) + 1):
            if i % j == 0: check = False; break
        if check == True: answer += 1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))