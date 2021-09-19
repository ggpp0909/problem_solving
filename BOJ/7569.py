import sys

from collections import deque
M, N, H = map(int, sys.stdin.readline().rstrip().split()) # 가로, 세로, 높이
arr = [[list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)] for j in range(H)]
visited = [[[False for i in range(M)] for j in range(N)] for k in range(H)]

di = [1, -1, 0, 0, 0, 0]
dj = [0, 0, 1, -1, 0, 0]
dk = [0, 0, 0, 0, 1, -1]

que = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                que.append([i, j, k])
                visited[i][j][k] = True

depth = 0
while que:
    size = len(que)

    for _ in range(size):
        x = que[0][2]
        y = que[0][1]
        z = que[0][0]
        que.popleft()

        for i in range(6):
            nx = x + di[i]
            ny = y + dj[i]
            nz = z + dk[i]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and visited[nz][ny][nx] == False and arr[nz][ny][nx] == 0:
                que.append([nz, ny, nx])
                visited[nz][ny][nx] = True

    depth += 1

ans = depth - 1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0 and visited[i][j][k] == False:
                ans = -1
                break

print(ans)