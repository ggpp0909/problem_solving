from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    outline = [[5 for i in range(200)] for j in range(200)]
    characterX, characterY, itemX, itemY  = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY
    def draw_ractangle(r1, c1, r2, c2):
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if r1 < i < r2 and c1 < j < c2:  # 내부일 때
                    outline[i][j] = 0
                elif outline[i][j] != 0:  # 테두리일 때 그리고 이미 내부가 아닐 때
                    outline[i][j] = 1  # 테투리랑 내부랑 겹치면 그건 내부

            
    # 직사각형 모두 그리기
    for i in rectangle:
        draw_ractangle(2 * i[0], 2 * i[1], 2 * i[2], 2 * i[3])

    

    # outline = [[0 for i in range(200)] for j in range(200)]
    # # 좌 -> 우
    # for i in range(150):
    #     for j in range(150):
    #         if arr[i][j + 1] == arr[i][j] ^ 1:
    #             outline[i][j] = arr[i][j]
    #             outline[i][j + 1] = arr[i][j + 1]


    # # 상 -> 하
    # for i in range(150):
    #     for j in range(150):
    #         if arr[j][i] == arr[j + 1][i] ^ 1:
    #             outline[j][i] = arr[j][i]
    #             outline[j + 1][i] = arr[j + 1][i]

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
    # print(arr)
    # print(outline)
    # 캐릭터에서 시작해서 아이템 먹을때까지 bfs
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    que = deque()
    visited = [[False for i in range(200)] for j in range(200)]
    que.append([characterX, characterY, 0])
    visited[characterX][characterY] = True

    while que:
        x, y, d = que.popleft()
        # print(x, y, itemX, itemY)
        if x == itemX and y == itemY:
            print(d // 2)
            return d // 2

        cnt = 0
        for dir in range(4):
            nx = x + di[dir]
            ny = y + dj[dir]
            # print(nx, ny)

            if 0 <= nx < 200 and 0 <= ny < 200 and outline[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append([nx, ny, d + 1])
                

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)
solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)
solution([[1,1,5,7]], 1, 1, 4, 7)
solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10)
solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3)
