from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    arr = [[0 for i in range(60)] for j in range(60)]

    def draw_ractangle(r1, c1, r2, c2):
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] = 1

            
    # 직사각형 모두 그리기
    for i in rectangle:
        draw_ractangle(i[0], i[1], i[2], i[3])

    
    # 상하좌우에서 한번씩 휩쓸면서 바깥 선 그리기
    outline = [[0 for i in range(51)] for j in range(51)]
    # 좌 -> 우
    for i in range(51):
        for j in range(51):
            if arr[i][j + 1] == arr[i][j] ^ 1:
                outline[i][j] = arr[i][j]
                outline[i][j + 1] = arr[i][j + 1]


    # 상 -> 하
    for i in range(51):
        for j in range(51):
            if arr[j][i] == arr[j + 1][i] ^ 1:
                outline[j][i] = arr[j][i]
                outline[j][i + 1] = arr[j][i + 1]

    # # 우 -> 좌
    # for i in range(50, -1, -1):
    #     for j in range(50, -1, -1):
    #         if arr[i][j] == 1:
    #             outline[i][j] = 1
    #             break
    
    # # 하 -> 상
    # for i in range(50, -1, -1):
    #     for j in range(50, -1, -1):
    #         if arr[j][i] == 1:
    #             outline[j][i] = 1
    #             break
    print(arr)
    print(outline)
    # 캐릭터에서 시작해서 아이템 먹을때까지 bfs
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    que = deque()
    visited = [[False for i in range(51)] for j in range(51)]
    que.append([characterX, characterY, 0])
    visited[characterX][characterY] = True

    while que:
        x, y, d = que.popleft()

        if x == itemX and y == itemY:
            print(d)
            return d

        for dir in range(4):
            nx = x + di[dir]
            ny = y + dj[dir]

            if 0 <= nx < 51 and 0 <= ny < 51 and outline[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append([nx, ny, d + 1])




    answer = 0
    return answer

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)