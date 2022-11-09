def solution(m, n, board): #높이 m 폭 n
    arr = []

    for i in range(len(board)):
        arr.append(list(board[i]))

    while True:
        visited = [[False for i in range(n)] for j in range(m)]
        flag = 0

        for i in range(m - 1):
            for j in range(n - 1):
                if arr[i][j] != 0 and arr[i][j] == arr[i + 1][j] == arr[i][j + 1] == arr[i + 1][j + 1]:
                    visited[i][j] = visited[i + 1][j] = visited[i][j + 1] = visited[i + 1][j + 1] = True
                    flag = 1

        if flag == 0:
            break

        else:
            for i in range(m - 1, -1, -1):
                for j in range(n):
                    if visited[i][j]:
                        temp = i - 1
                        while temp >= 0 and visited[temp][j]:  # temp 가 범위밖으로 안나가면서,
                            temp -= 1

                        if temp < 0:  # 맨 위까지 올라갔을때까지 없다면
                            arr[i][j] = 0  # 터트리기만해
                        else:
                            arr[i][j] = arr[temp][j]
                            visited[temp][j] = True
                        # 되는 이유: visited처리가 안된 애들 땡겨오고 바로 visited처리를 하기때문에
                        # 2x2블록의 밑부분부터 위로 탐색을하면 visited가 아닌 바로 다음블록을 땡겨옴 -> 완탐돌리면서 쭉 땡김


                        # while temp >= 0 and arr[temp][j] == 0: # temp 가 범위밖으로 안나가면서 올라가다가 바로위에 만나는 알파벳찾기
                        #     temp -= 1
                        #
                        # if temp < 0: # 맨 위까지 올라갔을때까지 없다면
                        #     arr[i][j] = 0 # 터트리기만해
                        # else:
                        #     arr[i][j] = arr[temp][j] # 알파벳 찾았으면 그 알파벳으로 바꿔치기해주고 그 알파벳 자리 True처리 해야 다음 while에 안걸림
                        #     arr[temp][j] = 0

                        # 안되는 이유 while로 찾는 temp가 visited바로 위에 문자를 못찾음, 2x2의 밑부분부터 탐색하면 2x2의 윗부분을 temp로 봄

    ans = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                ans += 1

    return ans