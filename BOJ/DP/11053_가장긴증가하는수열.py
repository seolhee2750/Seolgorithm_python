# BOJ #11053 가장 긴 증가하는 수열

n = int(input())
permu = list(map(int, input().split()))
count = [1] # 첫 번째 숫자의 길이는 어차피 1이므로 미리 추가
counting = 0

def find(now):
    global counting
    for i in reversed(range(len(count))):
        if counting < count[i] and permu[i] < now:
            counting = count[i]

for i in range(1, n):
    find(permu[i])
    count.append(counting+1)
    counting = 0

print(max(count))
