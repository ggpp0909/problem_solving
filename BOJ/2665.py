import heapq

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

n = int(input())

arr = [input() for i in range(n)]
dist = [[9999 for i in range(n)] for j in range(n)]

que = []
heapq.heappush(que, [0, 0, 0])
dist[0][0] = 0

while que:
    d, i, j = heapq.heappop(que)

    if i == n - 1 and j == n - 1:
        print(d)
        break

    if dist[i][j] < d:
        continue

    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]
        if 0 <= ni < n and 0 <= nj < n:
            temp = 1 ^ int(arr[ni][nj])
            nd = d + temp

            if dist[ni][nj] > nd:
                dist[ni][nj] = nd
                heapq.heappush(que, [nd, ni, nj])
