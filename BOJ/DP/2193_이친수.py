# BOJ #2193 이친수

n = int(input())

if n == 1: print(1)
elif n == 2: print(1)
else:
    result = [1, 1]  # n이 0일 때, 1일 때를 미리 저장
    for i in range(2, n):
        result.append(result[i-2] + result[i-1])
    print(result[-1])