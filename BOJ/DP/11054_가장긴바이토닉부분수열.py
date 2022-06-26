import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
r_nums = list(reversed(nums))
memory1 = [0 for _ in range(n)]
memory2 = [0 for _ in range(n)]
answer = 0

memory1[0] = 1
for i in range(1, n):
    maxi = 0
    for j in range(i):
        if nums[j] < nums[i]:
            maxi = max(maxi, memory1[j])
    memory1[i] = maxi + 1

memory2[0] = 1
for i in range(1, n):
    maxi = 0
    for j in range(i):
        if r_nums[j] < r_nums[i]:
            maxi = max(maxi, memory2[j])
    memory2[i] = maxi + 1
memory2 = list(reversed(memory2))

for i in range(n):
    answer = max(answer, memory1[i] + memory2[i])

print(answer - 1)