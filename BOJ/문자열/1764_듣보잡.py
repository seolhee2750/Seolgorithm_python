n, m = map(int, input().split())
memory = dict()
answer = []

for _ in range(n): memory[input()] = 1
for _ in range(m):
    now = input()
    if memory.get(now) == 1: answer.append(now)

answer.sort()
print(len(answer))
print("\n".join(answer))


