import sys

n, m = map(int, sys.stdin.readline().strip().split())
s = dict()
cnt = 0

for _ in range(n):
    s[sys.stdin.readline().strip()] = True
for _ in range(m):
    now = sys.stdin.readline().strip()
    if s.get(now):
        cnt += 1
    if cnt == n:
        break

print(cnt)

"""
처음엔 리스트로 넣어서 풀어주었으나,
리스트에 어떠한 값의 유무를 확인하는 경우에는 딕셔너리가 훨씬 효율적임
따라서 딕셔너리로 바꿔서 풀어주었더니 시간 훨씬 좋아짐
"""