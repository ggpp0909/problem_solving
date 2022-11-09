import sys
from collections import deque
# sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
# K 개 이상 광물 탐색(조건)을 만족하는 최소D?
# 조건을 만족하는 최적의 값 -> 매개변수탐색?
s = 0
e = 100000000

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# def dfs(i, j, cnt):
#     global flag
#     if cnt >= K:
#         flag = True

#     for dir in range(4):
#         ni = i + di[dir]
#         nj = j + dj[dir]

#         if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] <= mid:
#             visited[ni][nj] = True
#             cnt += 1
#             dfs(ni, nj)

ans = -1
while s <= e:
    mid = (s + e) // 2
    visited = [[False for i in range(M)] for j in range(N)]
    que = deque()
    flag = False
    cnt = 0
    
    for j in range(0, M):
        if arr[0][j] > mid:
            continue
        # # if flag:
        # #     break
        visited[0][j] = True
        # dfs(0, j, 1)
        que.append([0, j])
        cnt += 1
        

    for i in range(1, N):
        if arr[i][0] <= mid:
            cnt += 1
            visited[i][0] = True
            que.append([i, 0])
       
        # if flag:
        #     break
        # dfs(i, 0, 1)
        if arr[i][M - 1] <= mid:
            cnt += 1
            visited[i][M - 1] = True
            que.append([i, M - 1])

    
    # for i in range(0, N):
        # if arr[i][M - 1] > mid:
        #     continue
        # # if flag:
        # #     break
        # visited[i][M - 1] = True
        # dfs(i, M - 1, 1)
    
    # print(s, e, mid)
    while que:
        i, j = que.popleft()

        if cnt >= K:
            flag = True
            break
        
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and arr[ni][nj] <= mid:
                visited[ni][nj] = True
                # dfs(ni, nj, cnt + 1)
                cnt += 1
                que.append([ni, nj])


    # 채굴가능하면 일단 답 저장하고 더 최적의 값을 찾아
    if flag:
        ans = mid
        e = mid - 1
        # print("줄임")
    else:
        s = mid + 1

print(ans)