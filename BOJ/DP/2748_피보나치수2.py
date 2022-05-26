n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    fibo = [0, 1, 1]
    for i in range(3, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    print(fibo[-1])