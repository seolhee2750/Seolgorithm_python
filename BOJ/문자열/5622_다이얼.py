s = input()
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
dial = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
answer = 0
for i in s:
    answer += dial[alphabet.index(i)]
print(answer)

"""
두 번째 풀이

s = input()
nums = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
result = 0
for i in s:
    for j in range(len(nums)):
        if i in nums[j]:
            result += (3 + j)

print(result)
"""