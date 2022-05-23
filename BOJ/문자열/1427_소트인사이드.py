n = input()
n = sorted(n, reverse=True)
print(''.join(n))

"""
두 번째 풀이

print("".join(list(sorted(input()))[::-1]))
"""
