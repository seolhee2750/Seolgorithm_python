# BOJ #1302 베스트셀러

"""
tuple은 연산이 안됨 !!!
연산을 하고 싶으면 리스트로 만들어서 하자.
"""

import sys

n = int(sys.stdin.readline())
books = []
count = []
result = []

for _ in range(n):
    now = sys.stdin.readline().strip()
    if now in books:
        count[books.index(now)][1] += 1
    else:
        books.append(now)
        count.append([len(books)-1, 1])

count.sort(key = lambda x: x[1], reverse = True)

for i in range(len(count)):
    if count[i][1] == count[0][1]:
        result.append(books[count[i][0]])
    else:
        break

result.sort()
print(result[0])
