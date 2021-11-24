n, k = map(int, input().split())
memory = [[0]*(k+1) for _ in range(n+1)] # [n+1][k+1] 크기의 0으로 채워진 배열

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if w <= j: memory[i][j] = max(memory[i-1][j], memory[i-1][j-w]+v)
        else: memory[i][j] = memory[i-1][j]

print(memory[n][k])

