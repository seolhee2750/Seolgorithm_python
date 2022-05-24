# BOJ #5525 IOIOI
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
idx = 0
count = 0
result = 0

while idx <= m-2:
    if s[idx : idx+3] == "IOI":
        idx += 2
        count += 1
        if count == n:
            result += 1
            count -= 1
    else:
        idx += 1
        count = 0

print(result)

"""
원래는 그냥 s를 돌면서 n값에 따른 패턴을 그대로 찾아주는 방식을 사용했음
하지만 그렇게 하니까 2번 서브태스크를 통과하지 못했음
"IOI" 패턴을 인덱스를 두 칸씩 옮기면서 찾아주는게 훨씬 효율적임!!
"""