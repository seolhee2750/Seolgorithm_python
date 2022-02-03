a, b = map(int, input().strip().split(' '))
for i in range(0, b) :
    print("*"*a)

"""
[ 두 번째 풀이 ]

a, b = map(int, input().strip().split(' '))
tmp = ""
for i in range(b):
    for j in range(a):
        tmp += "*"
    print(tmp)
    tmp = ""
"""