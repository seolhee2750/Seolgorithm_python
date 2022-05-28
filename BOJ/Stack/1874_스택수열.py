import sys

n = int(sys.stdin.readline().strip())
nums = []
arr = []
new = []
answer = []
for i in range(n):
    num = int(sys.stdin.readline().strip())
    nums.append(num)

idx = 0
last = 0
over = False
while idx < n:
    if len(arr) == 0 or nums[idx] != arr[-1]:
        last += 1
        if last > n:
            over = True
            break
        arr.append(last)
        answer.append("+")
    else:
        idx += 1
        new.append(arr.pop())
        answer.append("-")
    if over:
        break

if over or new != nums:
    print("NO")
else:
    print("\n".join(answer))


