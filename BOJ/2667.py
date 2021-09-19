n = int(input())
arr = [input() for i in range(n)]
visited = [[False for i in range(n)] for j in range(n)]


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def recur(i, j):
    cnt = 1

    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == '1' and visited[ni][nj] == False:
            visited[ni][nj] = True
            cnt += recur(ni, nj)

    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and visited[i][j] == False:
            visited[i][j] = True
            ans.append(recur(i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)