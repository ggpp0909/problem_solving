import sys
import heapq
sys.stdin = open('input.txt')

T = int(input())

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for k in range(1, T + 1):
    n = int(input())
    arr = [input() for i in range(n)]
    dist = [[99999999 for i in range(n)] for j in range(n)]

    que = []
    dist[0][0] = 0
    heapq.heappush(que, (0, 0, 0))  # que에 시작노드에서의 가중치, 인덱스를 넣음

    while que:
        d, i, j = heapq.heappop(que)  # 가중치, 인덱스 꺼내

        if i == n - 1 and j == n - 1:
            ans = d
            break

        if dist[i][j] < d:  # 기존에있는 가중치가 지금꺼낸 가중치보다 작다면? 그냥 넘어가
            continue

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < n and 0 <= nj < n:
                nd = d + int(arr[ni][nj])
                if nd < dist[ni][nj]:  # 내가 가려고 하는곳 이 현재까지 온 가중치 + 현재에서 가려고하는 가중치보다 작다면 업데이트
                    dist[ni][nj] = nd
                    heapq.heappush(que, (nd, ni, nj))  # 지금 내가 가려고 하는곳을 que에 넣어( 후에 이섬에서 다른 갈 곳이 있는지 확인하기위해)

    print('#{} {}'.format(k, ans))

