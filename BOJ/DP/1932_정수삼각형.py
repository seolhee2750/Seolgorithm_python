n = int(input())
memory = [int(input())]

for _ in range(1, n):
    now = list(map(lambda x: int(x), input().split()))
    for i in range(len(now)):
        if i == 0:
            now[0] += memory[0]
        elif i == len(now)-1:
            now[-1] += memory[-1]
        else:
            if memory[i-1] > memory[i]: now[i] += memory[i-1]
            else: now[i] += memory[i]
    memory = now

print(max(memory))