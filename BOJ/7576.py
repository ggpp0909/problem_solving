import sys

from collections import deque
M, N= map(int, sys.stdin.readline().rstrip().split()) # 가로, 세로, 높이
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]
visited = [[False for i in range(M)] for j in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


que = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que.append([i, j])
            visited[i][j] = True

depth = 0
while que:
    size = len(que)
    for _ in range(size):
        x = que[0][1]
        y = que[0][0]
        que.popleft()

        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]

            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == False and arr[ny][nx] == 0:
                que.append([ny, nx])
                visited[ny][nx] = True

    depth += 1

ans = depth - 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == False:
            ans = -1
            break

print(ans)