s = input()
alphabet = list("abcdefghijklmnopqrstuvwxyz")
answer = [-1]*26
for i in s:
    if answer[alphabet.index(i)] == -1:
        answer[alphabet.index(i)] = s.index(i)
print(" ".join(list(map(lambda x: str(x), answer)))) # join은 [문자열] 타입일 때만 가능!
