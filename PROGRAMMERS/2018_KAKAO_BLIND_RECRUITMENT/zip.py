def solution(msg):
    # A ~ Z 초기값
    zip = [0] # 인덱스 맞추기위해 (나중에 ans에 인덱스를 append, index가 곧 색인번호)
    for i in range(1,27):
        zip.append(chr(64 + i))

    ans = []
    idx = 0
    # num = 27
    while idx <= len(msg) - 1: # idx가 끝인덱스 갔을때까지 돌려
        # for i in range(len(zip) - 1, -1, -1):
        #     size = len(zip[i][0])
        #     for j in range(size):
        #         flag = 1
        #         if zip[i][0][j] != msg[idx + j]:
        #             flag = 0
        #     if flag:
        #         temp_ans = zip[i][1]
        #         ans.append(zip[i][1])
        #         zip.append((msg[idx:size + 1], num))
        #         num += 1
        #         idx += size + 1
        #         break
        for i in range(1, len(msg) - idx + 1): # end가 slicing의 끝이기 때문에 +1 필요
            end = idx + i
            if msg[idx:end] in zip: # msg의 시작부터 끝이 zip에 있다면 temp 저장
                temp = msg[idx:end]

        code = zip.index(temp) # temp의 인덱스가 곧 색인번호
        ans.append(code)

        idx += len(temp) # temp의 길이만큼 시작위치 땡겨
        # print(temp)
        if idx <= len(msg) - 1:   # 만약 땡긴 idx가 범위내에있다? zip에 새로운 색인번호 추가해
            zip.append(temp + msg[idx])

    # print(ans)
    return ans

# solution('TOBEORNOTTOBEORTOBEORNOT')
solution('KAKAO')
