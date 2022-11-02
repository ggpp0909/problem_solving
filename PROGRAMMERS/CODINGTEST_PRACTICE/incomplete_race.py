def solution(participant, completion):
    temp = dict()
    for i in completion:
        if temp.get(i):
            temp[i] += 1
        else:
            temp[i] = 1
    
    for i in participant:
        if temp.get(i):
            temp[i] -= 1
            continue
        else:
            return i