import heapq

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
casenum = 0

while True:
    casenum += 1
    N = int(input())
    if N == 0:
        break

    arr = [list(map(int, input().split())) for i in range(N)]

    dist = [[999999999 for i in range(N)] for j in range(N)]

    que = []
    heapq.heappush(que, [arr[0][0], 0, 0])
    dist[0][0] = arr[0][0]

    while que:
        d, i, j = heapq.heappop(que)

        if dist[i][j] < d:
            continue

        if i == N - 1 and j == N - 1:
            print('Problem {}: {}'.format(casenum, d))
            break

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < N and 0 <= nj < N:
                nd = d + arr[ni][nj]
                if dist[ni][nj] > nd:
                    dist[ni][nj] = nd
                    heapq.heappush(que, [nd, ni, nj])
