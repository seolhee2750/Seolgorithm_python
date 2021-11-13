"""
재귀와 DP 메모이제이션 방식을 함께 사용하는 문제!
"""

memory = [[[0]*21 for _ in range(21)] for __ in range(21)]

def w(a, b, c):
    if (a <= 0) | (b <= 0) | (c <= 0):
        return 1
    if (a > 20) | (b > 20) | (c > 20):
        return w(20, 20, 20)
    if memory[a][b][c]:
        return memory[a][b][c] # 이미 abc 값에 해당하는 memory 자리에 값이 할당되어 있다면(0이 아니라면), 연산 필요 없으므로 그대로 memory[a][b][c] 값을 리턴!
    if a < b < c:
        memory[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a,  b-1, c)
        return memory[a][b][c]
    memory[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memory[a][b][c]

while True:
    n = list(map(lambda x: int(x), input().split()))
    if n == [-1, -1, -1]: break
    print(f"w({n[0]}, {n[1]}, {n[2]}) = {w(n[0], n[1], n[2])}")
