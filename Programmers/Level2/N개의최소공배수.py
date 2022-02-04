def solution(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                a = arr[i]
                b = arr[i + 1]
            else:
                a = arr[i + 1]
                b = arr[i]
            for j in range(b, a * b + 1):
                if j % a == 0 and j % b == 0:
                    arr[i + 1] = j
                    break

        return arr[-1]

print(solution([1, 6, 8, 14]))