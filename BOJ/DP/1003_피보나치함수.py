"""
n이 0일 때 [1, 0]
n이 1일 때 [0, 1]
=> n의 0, 1 호출 횟수는 n-1과 n-2의 0, 1 호출 횟수를 더한 값과 같음
==> n이 0일 경우 [1, 0], n이 1일 경우 [0, 1] ~> n이 2일 경우는 [1+0, 0+1]

찾을 n들을 모두 입력받은 후, 그 중 가장 큰 수를 찾아서 그 수까지 모든 수의 0, 1의 출력 횟수를 구해서 배열로 만들어 놓음
그 다음 입력받았던 nums 배열을 순서대로 돌며 해당 수의 자리에 들어있는 배열 요소를 출력해주었음
"""

t = int(input())
nums = []
for i in range(t): nums.append(int(input()))

memory = []
for i in range(max(nums)+1):
    if i == 0: memory.append([1, 0])
    elif i == 1: memory.append([0, 1])
    else: memory.append([memory[i-1][0]+memory[i-2][0], memory[i-1][1]+memory[i-2][1]])

for i in nums: print(" ".join(list(map(lambda x: str(x), memory[i]))))