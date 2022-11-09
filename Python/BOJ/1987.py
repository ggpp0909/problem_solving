R, C = map(int, input().split())
arr = [input() for i in range(R)]

visited = [0 for i in range(100)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

ans = 0
print(ord(arr[0][0]))
visited[ord(arr[0][0])] = True

def recur(cnt, i, j):
    global ans
    ans = max(ans, cnt)

    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < R and 0 <= nj < C and not visited[ord(arr[ni][nj])]:
            visited[ord(arr[ni][nj])] = True
            recur(cnt + 1, ni, nj)
            visited[ord(arr[ni][nj])] = False

recur(1, 0, 0)
print(ans)
