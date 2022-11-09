H, W = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(H)]


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def bfs():
    visited = [[False for i in range(W)] for j in range(H)]
    que = []
    que.append([0, 0])
    visited[0][0] = True
    cnt = 0

    while que:
        i = que[0][0]
        j = que[0][1]
        que.pop(0)

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj]:
                if arr[ni][nj] == 0:    # 치즈가 아니면 이동
                    que.append([ni, nj])
                    visited[ni][nj] = True
                else:
                    cnt += 1            # 치즈면 바꾸기만해
                    arr[ni][nj] = 0
                    visited[ni][nj] = True
    return cnt

cnt = '#'
ans = []
while cnt:
    cnt = dfs()
    ans.append(cnt)

print(len(ans) - 1)
print(ans[-2])