from collections import deque

H, W = map(int, input().split())
arr = [input() for i in range(H)]
ans = 0

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'L':
            visited = [[False for i in range(W)] for j in range(H)]
            visited[i][j] = True
            que = deque()
            depth = 0
            que.append([i, j, depth])

            while que:
                x = que[0][0]
                y = que[0][1]
                depth = que[0][2]
                que.popleft()

                for dir in range(4):
                    ni = x + di[dir]
                    nj = y + dj[dir]

                    if 0 <= ni < H and 0 <= nj < W and visited[ni][nj] == False and arr[ni][nj] == 'L':
                        visited[ni][nj] = True
                        que.append([ni, nj, depth + 1])

                if len(que) == 0: # 마지막이라면, 이곳에 쓴이유 : 앞에쓰면 처음에 꺼내자마자 조건에 걸림
                    ans = max(ans, depth)
                    break

print(ans)