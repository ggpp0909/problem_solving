from collections import deque

n, m = map(int, input().split())
maze = [input() for i in range(n)]

visited = [[[0 for i in range(2)] for j in range(m)] for k in range(n)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

que = deque()
que.append([0, 0, 1, 0]) # i, j, depth, wall
visited[0][0][0] = 1
ans = -1
while que:
    temp = que.popleft()
    i = temp[0]
    j = temp[1]
    depth = temp[2]
    wall = temp[3]

    if i == n - 1 and j == m - 1:
        ans = depth
        break

    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        # 벽을 안부순 상태
        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj][1] == 0 and maze[ni][nj] == '1' and wall == 0:
            visited[ni][nj][1] = 1
            que.append([ni, nj, depth + 1, 1])

            # 벽을 부순 상태
        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj][wall] == 0 and maze[ni][nj] == '0':
            visited[ni][nj][wall] = 1
            que.append([ni, nj, depth + 1, wall])

print(ans)