s = list(input())
answer = []
check = False
tmp = ""

for i in s:
    if i == " ":
        if check == False:
            answer.append(tmp[::-1] + " ")
            tmp = ""
        else: tmp += " "
    elif i == "<":
        check = True
        if len(tmp) > 0: answer.append(tmp[::-1])
        tmp = "<"
    elif i == ">":
        check = False
        answer.append(tmp + ">")
        tmp = ""
    else: tmp += i
if len(tmp) > 0: answer.append(tmp[::-1])

print("".join(answer))