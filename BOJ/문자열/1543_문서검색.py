# BOJ #1543 문서 검색

doc = input()
text = input()
result = 0
idx = 0

while idx <= len(doc) - len(text):
    if doc[idx : idx + len(text)] == text:
        result += 1
        idx += len(text)
    else:
        idx += 1

print(result)