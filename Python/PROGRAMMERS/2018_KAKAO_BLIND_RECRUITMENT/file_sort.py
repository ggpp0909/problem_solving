def solution(files):
    arr = []

    for i in files:
        original = i
        i = i.upper() + '#'
        # print(i)

        flag = 0
        # tail = '' # tail은 빈문자열이 될 수도 있음
        for j in range(len(i)):
            if i[j].isdigit() and not flag: # 숫자가 처음 나오면 그 인덱스까지 head, 그인덱스는 num의 첫인덱스이므로 temp에 저장
                head = i[:j]
                temp = j
                flag = 1

            if flag and not i[j].isdigit(): # 숫자가 나온적이 있고 숫자가 아니라면 number 슬라이싱
                number = i[temp:j]
                # tail = i[j:]
                break

        # print(head, number, tail)
        arr.append((head, int(number), original))
    arr.sort(key=lambda x: (x[0], x[1]))

    ans = []
    for i in arr:
        ans.append(i[2])
    # print(temp)
    # print(ans)

    return ans



solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])