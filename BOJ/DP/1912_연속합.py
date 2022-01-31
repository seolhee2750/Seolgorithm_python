# BOJ #1912 연속합
import sys
sys.setrecursionlimit(1000000)

n = int(input())
nums = list(map(int, input().split()))
sums = [nums[0]]

for i in range(1, n):
    if nums[i] < sums[-1] + nums[i]:
        sums.append(sums[-1] + nums[i])
    else:
        sums.append(nums[i])

print(max(sums))