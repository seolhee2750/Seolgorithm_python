import sys

n = int(sys.stdin.readline().strip())
if n == 1:
    print(10)
else:
    memory = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(n-1):
        for j in range(9):
            memory[j + 1] = (memory[j] + memory[j + 1]) % 10007
    print(memory[-1])