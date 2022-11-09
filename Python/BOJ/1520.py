import sys
sys.setrecursionlimit(10**6)

M, N = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(M)]
visited = [[False for i in range(N)] for j in range(M)]
dp = [[-1 for i in range(N)] for j in range(M)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
cnt = 0
visited[0][0] = True
dest = arr[M-1][N-1]

def dfs(i=0, j=0):
    global cnt, dest

    if i == M - 1 and j == N - 1:
        # cnt += 1
        return 1

    # 메모이제이션
    if dp[i][j] != -1:
        return dp[i][j]

    ret = 0
    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == False and arr[i][j] > arr[ni][nj]:
            visited[ni][nj] = True
            # dfs(ni, nj)
            ret += dfs(ni, nj)
            visited[ni][nj] = False
    dp[i][j] = ret
    return ret

print(dfs())