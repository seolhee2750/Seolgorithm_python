def solution(lottos, win_nums):
    zero = 0
    count = 0
    rank = [6, 5, 4, 3, 2]
    for i in lottos:
        if i == 0: zero += 1
        elif i in win_nums: count += 1
    return [rank.index(count + zero)+1 if count + zero > 1 else 6, rank.index(count)+1 if count > 1 else 6]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))