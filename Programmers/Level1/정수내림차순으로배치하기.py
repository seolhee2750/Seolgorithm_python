def solution(n):
    n = list(str(n))
    n.sort(reverse = True)
    return int(''.join(n))

print(solution(118372))

# 리스트 형 변환 : 굳이 map 안써도 list(str(n)) 이런식으로 가능
# sort 할 때는 sort만 꼭 따로 빼서 해주기. 안그러면 적용 안됨