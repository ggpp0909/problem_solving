import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque
sys.setrecursionlimit(10 ** 6)

def rotate(original_arr, L): # 90도 회전
    arr = [[0 for i in range(2 ** N)] for j in range(2 ** N)]
    for i in range(0, 2 ** N, 2 ** L):
        for j in range(0, 2 ** N, 2 ** L):
            for i2 in range(2 ** L):
                for j2 in range(2 ** L):
                    arr[i + j2][j + 2 ** L - i2 - 1] = original_arr[i + i2][j + j2]
    return arr

def melt():
    temp = []
    for i in range(2 ** N):
        for j in range(2 ** N):
            cnt = 0
            for dir in range(4):
                ni = i + di[dir]
                nj = j + dj[dir]
                # 인접한 얼음이 3개 이상이라면 일단 리스트에 저장: 바로 안지우고 일단 저장하는 이유 -> 지금 지워서 0되면 다음상황에 지장이 생김, 한번에 지워야해
                if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and arr[ni][nj]:
                    cnt += 1
                # 인접한 얼음이 3개 이상이 아니면 녹여
            if cnt <= 2:
                temp.append([i, j])

    for i in range(len(temp)):
        x, y = temp[i][0], temp[i][1]
        if arr[x][y]:
            arr[x][y] -= 1

# def dfs(i, j):
#     global size
#
#     for dir in range(4):
#         ni = i + di[dir]
#         nj = j + dj[dir]
#         if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and visited[ni][nj] == False and arr[ni][nj]:
#             visited[ni][nj] = True
#             size += 1
#             dfs(ni, nj)


from collections import deque

N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(2 ** N)]
L = list(map(int, input().split()))
visited = [[False for i in range(2 ** N)] for j in range(2 ** N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for i in range(len(L)):
    # pprint(arr)
    arr = rotate(arr, L[i])
    # pprint(arr)
    melt()
    # pprint(arr)

sum = 0
link_cnt = 0
for i in range(2 ** N):
    for j in range(2 ** N):
        sum += arr[i][j]
        if arr[i][j] and visited[i][j] == False:
            visited[i][j] = True
            que = deque()
            que.append([i, j])
            size = 1
            while que:
                x = que[0][0]
                y = que[0][1]
                que.popleft()
                for dir in range(4):
                    ni = x + di[dir]
                    nj = y + dj[dir]
                    if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and visited[ni][nj] == False and arr[ni][nj]:
                        visited[ni][nj] = True
                        size += 1
                        que.append([ni, nj])

            link_cnt = max(link_cnt, size)

print(sum)
print(link_cnt)