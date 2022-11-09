import sys
sys.stdin = open('input.txt')

def go(i, j): # i ,j에서 갈수 있는 길을 찾아서 이동하는 함수 근데 2를 만나면 리턴
    global ans
    if maze[i][j] == 2:
        ans = 1
        return

    if ans:
        return

    visited[i][j] = True  # 갔던길은 표시하기 like 헨젤과그레텔
    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]
        if 0 <= ni < leng and 0 <= nj < leng and maze[ni][nj] != 1 and visited[ni][nj] == False:
            go(ni, nj)
            visited[i][j] = False

n = int(input())
for k in range(1, n + 1):
    leng = int(input())
    maze = [list(map(int, input())) for i in range(leng)]
    visited = [[False for i in range(leng)] for j in range(leng)]

    ans = 0
    # 시작점 좌표 찾기
    for i in range(leng):
        for j in range(leng):
            if maze[i][j] == 3:
                start_i = i
                start_j = j

    # 상 우 하 좌
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    go(start_i, start_j)

    print('#{} {}'.format(k, ans))

