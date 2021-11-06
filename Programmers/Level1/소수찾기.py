def solution(n):
    if n == 2: return 1
    elif n == 3: return 2
    else:
        answer = 2
        for i in range(4, n+1):
            check = True
            for j in range(2, int(i**(1/2))+1):
                if i % j == 0: check = False; break
            if check == True: answer += 1
        return answer

print(solution(10))
print(solution(5))

# 다른 사람 문제 풀이 (에라토스테네스의 체) => 공부 필요!
"""
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
"""