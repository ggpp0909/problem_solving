import sys
sys.stdin = open('input.txt')

n = int(input())
for k in range(1, n + 1):
    leng = int(input())
    maze = [list(map(int, input())) for i in range(leng)]
    visited = [[-1 for i in range(leng)] for j in range(leng)]

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
    try:
        while que:
            i, j = que.pop(0)
            if visited[i][j] == -1:     # 시작 노드 처리
                visited[i][j] = 0

            if maze[i][j] == 3:
                ans = visited[i][j] - 1
                break

            for dir in range(4):
                ni = i + di[dir]
                nj = j + dj[dir]
                if 0 <= ni < leng and 0 <= nj < leng and maze[ni][nj] != 1 and visited[ni][nj] == -1:
                    que.append([ni, nj])
                    visited[ni][nj] = visited[i][j] + 1     # 갔던길은 표시하기 like 헨젤과그레텔
    except:     # 경로가 없다 -> 무한 반복문이므로, 빈리스트에서 pop을 하므로 오류 발생
        ans = 0

    print('#{} {}'.format(k, ans))