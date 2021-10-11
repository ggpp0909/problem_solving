

def solution(msg):
    # A ~ Z 초기값
    zip = []
    for i in range(1,27):
        zip.append((chr(64 + i), i))

    ans = []
    idx = 0
    num = 27
    while idx <= len(msg):
        for i in range(len(zip) - 1, -1, -1):
            size = len(zip[i][0])
            for j in range(size):
                flag = 1
                if zip[i][0][j] != msg[idx + j]:
                    flag = 0
            if flag:
                ans.append(zip[i][1])
                zip.append((msg[idx:size + 1], num))
                num += 1
                idx += size + 1

    print(ans)








    answer = []
    return answer

# solution('TOBEORNOTTOBEORTOBEORNOT')
solution('KAKAO')
