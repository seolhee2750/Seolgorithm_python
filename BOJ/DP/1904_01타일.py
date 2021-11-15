""""
n == 1 : 1
n == 2 : 00, 11
n == 3 : 001, 100, 111
n == 4 : 0000, 0011, 1001, 1100, 1111
n == 5 : 00001, 00111, 10011, 11001, 11100, 10000, 00100, 11111
==> p(n) = p(n-2) + p(n-1)
"""

n = int(input())
if n == 1: print(1)
elif n == 2: print(2)
else:
    memory = [1, 2]
    for i in range(2, n):
        memory.append((memory[i-2] + memory[i-1]) % 15746)
    print(memory[n-1])
