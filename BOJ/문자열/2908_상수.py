nums = list(map(lambda x: int(x[::-1]), input().split()))
print(max(nums))

# reverse는 list에만 적용 가능, reversed는 str에도 적용 가능.
# 두 함수 모두 list 형태로 반환!

# 문자열을 그대로 뒤집으려면 [::-1] 쓰는게 제일 편함.
# slice는 [시작인덱스:끝인덱스:간격] 이렇게 표시해주면 됨!
# 시작 인덱스가 0이거나 끝 인덱스가 마지막 인덱스일 경우 생략이 가능하고, 간격은 마이너스로 표시할 시 역순으로 반환해준다.