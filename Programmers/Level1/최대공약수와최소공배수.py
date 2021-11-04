def solution(n, m):
    if n < m:
        min = n; max = m
    else:
        min = m; max = n

    # 최대공약수
    gcd = min
    while gcd > 0:
        if (max % gcd == 0) & (min % gcd == 0):
            break
        else:
            gcd -= 1

    # 최소공배수
    lcm = max
    while True:
        if (lcm % min == 0) & (lcm % max == 0):
            break
        else:
            lcm += 1

    return [gcd, lcm]

print(solution(3, 12))
print(solution(1, 10))