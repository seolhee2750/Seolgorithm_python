n = input()
answer = []

for i in range(0, len(n)):
    answer.append(n[i:])

answer.sort()
print("\n".join(answer))