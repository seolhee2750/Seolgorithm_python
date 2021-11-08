def solution(sizes):
    for i in range(0, len(sizes)): sizes[i].sort()
    max1 = 0
    max2 = 0
    for i in range(0, len(sizes)):
        if sizes[i][0] > max1: max1 = sizes[i][0]
        if sizes[i][1] > max2: max2 = sizes[i][1]
    return max1 * max2

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

# 다른 사람 풀이
"""
첫 번째)
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
    
두 번째)
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
"""

