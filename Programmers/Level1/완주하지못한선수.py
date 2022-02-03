def solution(participant, completion):
    dictCompletion = dict()
    for i in completion:
        if dictCompletion.get(i) == None: dictCompletion[i] = 1
        else: dictCompletion[i] += 1
    for i in participant:
        if dictCompletion.get(i) == None: return i; break
        elif dictCompletion.get(i) > 0: dictCompletion[i] -= 1
        else: return i; break

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

"""
[ 두 번째 문제 풀이 ]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    
    for i in range(len(participant)):
        if (i == len(participant)-1) or participant[i] != completion[i]:
            answer = participant[i]
            break
    
    return answer
"""