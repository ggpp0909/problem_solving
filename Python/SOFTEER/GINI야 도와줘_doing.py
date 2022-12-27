from collections import deque
R, C = map(int, input().split())
arr = [input() for i in range(R)]
visited = [[False for i in range(C)] for j in range(R)]
# 방향벡터
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# 시작, 도착 좌표 초기화
si = sj = ei = ej = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == "W":
            si = i
            sj = j
        elif arr[i][j] == "H":
            ei = i
            ej = j

que = deque()
que.append([si, sj, 0])

while que:
    i, j, depth = que.popleft()

    if i == ei and j == ej:
        print(depth)
        break

    for dir in range(4):
        ni = i + di[dir]
        nj = j + di[dir]

        if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and arr[ni][nj] == ".":
            visited[ni][nj] = True
            que.append([ni, nj, depth + 1])

else: print("FAIL")