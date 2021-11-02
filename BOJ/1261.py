import heapq

M, N = map(int, input().split())
arr = [input() for i in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

dist = [[99999 for i in range(M)] for j in range(N)]

que = []
heapq.heappush(que, [0, 0, 0])
dist[0][0] = 0

while que:
    d, i, j = heapq.heappop(que)

    if i == N - 1 and j == M - 1:
        print(d)
        break

    if d > dist[i][j]:
        continue

    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < N and 0 <= nj < M:
            nd = d + int(arr[ni][nj])
            if dist[ni][nj] > nd:
                dist[ni][nj] = nd
                heapq.heappush(que, [nd, ni, nj])