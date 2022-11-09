N, M = map(int, input().split())
maze = [input() for i in range(N)]
visited = [[1 for i in range(M)] for j in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

visited[0][0] = 1
que = [[0, 0]]
ans = 1
def bfs():
    global ans
    while que:
        temp = que.pop(0)
        if temp[0] == N - 1 and temp[1] == M - 1:
            ans = visited[temp[0]][temp[1]]
            break

        for k in range(4):
            ni = temp[0] + di[k]
            nj = temp[1] + dj[k]

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 1 and int(maze[ni][nj]):
                visited[ni][nj] = visited[temp[0]][temp[1]] + 1
                que.append([ni ,nj])

bfs()
print(ans)