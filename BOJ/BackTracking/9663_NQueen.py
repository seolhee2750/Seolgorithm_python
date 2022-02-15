# BOJ 9663 N-Queen (백트래킹 대표예제)

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