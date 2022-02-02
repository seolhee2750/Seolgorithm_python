# BOJ #11727 2*n 타일링

n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    memory = [1, 3]
    for i in range(2, n):
        memory.append((memory[i-2]*2 + memory[i-1]) % 10007)
    print(memory[-1])