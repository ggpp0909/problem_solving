from collections import deque
M, N, K = map(int, input().split())

arr = [[True for i in range(M)] for j in range(N)]

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())

    for i in range(lx, rx):
        for j in range(ly, ry):
            arr[i][j] = False

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

visited = [[False for i in range(M)] for j in range(N)]
ans = []
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == True and not visited[i][j]:
#             que = deque()
#             que.append([i, j])
#             visited[i][j] = True
#             cnt = 0
#             while que:
#                 cur_i, cur_j = que.popleft()
#                 cnt += 1

#                 for dir in range(4):
#                     ni = cur_i + di[dir]
#                     nj = cur_j + dj[dir]

#                     if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == True and not visited[ni][nj]:
#                         visited[ni][nj] = True
#                         que.append([ni, nj])
#             ans.append(cnt)

def dfs(i, j):
    global cnt
    cnt += 1
    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == True and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj)

for i in range(N):
    for j in range(M):
        if arr[i][j] == True and not visited[i][j]:
            visited[i][j] = True
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
print(*ans)