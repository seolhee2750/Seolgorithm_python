# BOJ 9663 N-Queen (백트래킹 대표예제)

"""
현재 이 문제는 파이썬으로 평범하게 백트래킹으로 풀 시 무조건 시간초과
=> https://www.acmicpc.net/source/37836327 이 풀이 참고해서 다시 공부해보기.
"""

n = int(input())
count = 0
row = [0]*n
check = True

def dfs(x):
    global count
    global check

    if x == n:
        count += 1
    else:
        for i in range(n):
            row[x] = i
            for j in range(x):
                if row[j] == row[x] or abs(row[j] - row[x]) == abs(j - x):
                    check = False
                    break
            if check == True:
                dfs(x + 1)
            else:
                check = True

dfs(0)
print(count)