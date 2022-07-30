from collections import deque
# BOJ 2206 벽부수고 이동하기와 유사
N, M = map(int, input().split())
arr = [list(input()) for i in range(N)]
visited = [[[0 for i in range(1 << 6)] for j in range(M)] for k in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# # 키를 가지고 있는가를 배열의 인덱스로 매칭하기 위함
key = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5
}

door = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
    "F" : 5
}

s_i = s_j = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == "0":
            s_i = i
            s_j = j
            arr[i][j] = "."
            break

que = deque()
que.append([s_i, s_j, 0, 0]) # 행, 열, depth, 열쇠비트
ans = -1

while que:
    i, j, depth, keys = que.popleft()
    if arr[i][j] == "1":
        ans = depth
        break

    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj][keys]:
            # 빈 공간만 이동
            if arr[ni][nj] == "." or arr[ni][nj] == "1":
                visited[ni][nj][keys] = True
                que.append([ni, nj, depth + 1, keys])
            
            # 열쇠 먹기
            elif arr[ni][nj] in ["a", "b", "c", "d", "e", "f"]:
                temp = keys | (1 << key[arr[ni][nj]])
                visited[ni][nj][temp] = True
                que.append([ni, nj, depth + 1, temp])
            
            # 문열기
            elif arr[ni][nj] in ["A", "B", "C", "D", "E", "F"]:
                if keys & (1 << door[arr[ni][nj]]): # 해당 키를 갖고있다면?
                    visited[ni][nj][keys] = True
                    que.append([ni, nj, depth + 1, keys])


print(ans)