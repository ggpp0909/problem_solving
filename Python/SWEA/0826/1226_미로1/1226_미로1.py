import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    k = int(input())
    leng = 16
    maze = [list(map(int, input())) for i in range(leng)]
    visited = [[False for i in range(leng)] for j in range(leng)]

    # 시작점 좌표 찾기
    for i in range(leng):
        for j in range(leng):
            if maze[i][j] == 2:
                start_i = i
                start_j = j

    # 상 우 하 좌
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    # BFS
    que = [[start_i, start_j]]
    ans = 0
    while que:
        i, j = que.pop(0)
        if visited[i][j] == False:  # 시작 노드 처리
            visited[i][j] = True

        if maze[i][j] == 3:
            ans = 1
            break

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < leng and 0 <= nj < leng and maze[ni][nj] != 1 and visited[ni][nj] == False:
                que.append([ni, nj])
                visited[ni][nj] = True    # 갔던길은 표시하기 like 헨젤과그레텔

    print('#{} {}'.format(k, ans))