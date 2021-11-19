"""
어차피 새로 붙이는 알파벳들은 b와 잘 맞도록 넣을 것이므로
기존의 문자열을 자리를 옮겨가며 경우의 수를 모두 비교해본다.
"""

a, b = input().split()
cases = []

for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[j+i]: count += 1
    cases.append(count)

print(min(cases))