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

"""
딕셔너리를 사용한 이유
=> 리스트로 만들어서 검색해줄 수 있지만 딕셔너리의 get을 사용하여 검색 시 효율이 훨씬 올라감 !
"""


