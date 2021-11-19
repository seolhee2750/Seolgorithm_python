"""
30의 배수는
맨 마지막이 0으로 끝나야 하고, 모든 자라수의 합이 3으로 나눠져야 한다.
=> 숫자를 어떻게 조합하든 30의 배수가 될지 안될지는 이미 결정된 것,,!!
=> 입력받은 수를 내림차순 정렬하여 제일 큰 수를 만든 후, 위에서 말한 조건을 체크해주면 됨.
"""

n = sorted(input(), reverse=True)
sum = 0

for i in n: sum += int(i)

if (sum % 3 != 0) or ("0" not in n): print(-1)
else: print("".join(n))
