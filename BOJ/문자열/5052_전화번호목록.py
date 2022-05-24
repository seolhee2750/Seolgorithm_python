import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    nums = []
    for _ in range(n):
        nums.append(sys.stdin.readline().strip())
    nums.sort()
    check = True

    for i in range(0, n-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            check = False
            break

    if check:
        print("YES")
    else:
        print("NO")

"""
처음엔 2중 for문으로 일일이 검사해주다가 같은 접두사를 발견할 시 종료하는 식으로 구현했고, 시간초과 발생하였음
=> nums를 정렬하면 당연하게도 접두사가 같은 경우 앞, 뒤로 배치되기 때문에 2중 for문 사용하지 않고, 단순히 앞뒤만 검사해줌으로써 해결하였음
"""