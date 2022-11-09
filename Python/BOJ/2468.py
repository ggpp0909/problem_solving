import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, input().split())) for i in range(n)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

que = deque()
ans = 0
for k in range(101):
    visited = [[False for _ in range(n)] for __ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= k and not visited[i][j]:
                cnt += 1
                que.append([i, j])
                visited[i][j] = True

                while que:
                    x = que[0][0]
                    y = que[0][1]
                    que.popleft()

                    for dir in range(4):
                        ni = x + di[dir]
                        nj = y + dj[dir]

                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] >= k and not visited[ni][nj]:
                            que.append([ni, nj])
                            visited[ni][nj] = True
    ans = max(ans, cnt)

print(ans)