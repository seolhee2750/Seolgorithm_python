"""
p(1) = 1
p(2) = 1
p(3) = 1
p(4) = 2
p(5) = 2
p(6) = 3 = p(5) + p(1)
p(7) = 4 = p(6) + p(2)
p(8) = 5 = p(7) + p(3)
p(9) = 7 = p(8) + p(4)
p(10) = 9 = p(9) + p(5)

=> p(n) = p(n-1) + p(n-5)
"""

t = int(input())
memory = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
n = []
for _ in range(0, t): n.append(int(input()))

if max(n) > 10:
    num = 10
    while num < max(n):
        memory.append(memory[num-1] + memory[num-5])
        num += 1

for i in n: print(memory[i-1])
