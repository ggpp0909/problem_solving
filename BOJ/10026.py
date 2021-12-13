from collections import deque

N = int(input())

arr = [input() for i in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
# 정상인
def bfs1(i, j):
    color = arr[i][j]

    que = deque()
    que.append([i, j])
    visited[i][j] = True

    while que:
        i, j = que.popleft()

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == color and not visited[ni][nj]:
                visited[ni][nj] = True
                que.append([ni, nj])
# 적록색약
def bfs2(i, j):
    color = arr[i][j]
    is_GR = False
    if color == 'G' or color == 'R':
        is_GR = True

    que = deque()
    que.append([i, j])
    visited[i][j] = True

    while que:
        i, j = que.popleft()

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if is_GR and (arr[ni][nj] == 'G' or arr[ni][nj] == 'R'):
                    visited[ni][nj] = True
                    que.append([ni, nj])
                elif not is_GR and arr[ni][nj] == 'B':
                    visited[ni][nj] = True
                    que.append([ni, nj])

visited = [[False for i in range(N)] for j in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        bfs1(i, j)
        cnt1 += 1

visited = [[False for i in range(N)] for j in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        bfs2(i, j)
        cnt2 += 1

print(cnt1, cnt2)