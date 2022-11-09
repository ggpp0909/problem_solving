def solution(record):
    arr = []
    for i in record:
        arr.append(i.split(' '))

    id_nickname = {}
    for i in arr:
        if i[0] == 'Enter' or i[0] == 'Change':
            id_nickname[i[1]] = i[2]
    # print(id_nickname)

    answer = []
    for i in arr:
        if i[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(id_nickname[i[1]]))
        elif i[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(id_nickname[i[1]]))
    # print(answer)

    return answer


solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])