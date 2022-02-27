import sys
from collections import deque
# sys.setrecursionlimit(10**6)

# N, M = map(int, input().split())
# arr = [list(sys.stdin.readline().rstrip()) for i in range(N)]
#
# di = [1, 0, -1, 0]
# dj = [0, 1, 0, -1]
#
# def dfs(i, j):
#     global cnt
#     for dir in range(4):
#         ni = i + di[dir]
#         nj = j + dj[dir]
#
#         if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == "0" and not visited[ni][nj]:
#             visited[ni][nj] = True
#             cnt += 1
#             dfs(ni, nj)
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == "0":
#             cnt = 1
#             visited = [[False for i in range(M)] for j in range(M)]
#             visited[i][j] = True
#             dfs(i, j)
#             arr[i][j] = str(cnt)
#
# for i in arr:
#     print(''.join(i))

N, M = map(int, input().split())
arr = [list(sys.stdin.readline().rstrip()) for i in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

size = [0 for i in range(N * M + 1)]
num = 1
numarr = [[0 for i in range(M)] for j in range(N)]

def dfs(i, j, num):
    global cnt
    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == "0" and not visited[ni][nj]:
            visited[ni][nj] = True
            numarr[ni][nj] = num
            cnt += 1
            dfs(ni, nj, num)

def bfs(i, j, num):
    global cnt

    que = deque()
    que.append([i, j])

    while que:
        x, y = que.popleft()
        for dir in range(4):
            nx = x + di[dir]
            ny = y + dj[dir]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == "0" and not visited[nx][ny]:
                visited[nx][ny] = True
                numarr[nx][ny] = num
                cnt += 1
                que.append([nx, ny])


visited = [[False for i in range(M)] for j in range(M)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == "0" and not visited[i][j]:
            visited[i][j] = True
            numarr[i][j] = num
            cnt = 1
            bfs(i, j, num)
            size[num] = cnt
            num += 1

# print("arr", arr)
# print("numarr",numarr)
# print("size",size)
for i in range(N):
    for j in range(M):
        if arr[i][j] == "1":
            temp = 0
            tempset = set()
            for dir in range(4):
                ni = i + di[dir]
                nj = j + dj[dir]
                if 0 <= ni < N and 0 <= nj < M:
                    tempset.add(numarr[ni][nj])
            for k in tempset:
                temp += size[k]
                temp %= 10
            arr[i][j] = str((temp + 1) % 10)

for i in arr:
    print(''.join(i))