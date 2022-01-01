import sys
import heapq
sys.stdin = open('input.txt')

# 가중치가 존재할때 최단경로를 찾는 알고리즘 - 다익스트라
# 알고리즘에서는 heapq(최소힙)를 import해서 사용하여 간단하게 구현 가능
# 코드구조는 BFS와 유사

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())

for k in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    # 1. 모든 지점에서의 가중치를 무한대로 세팅
    dist = [[9999 for i in range(N)] for j in range(N)]

    # 2. 시작지점의 가중치를 0으로 세팅하고 출발
    que = []
    heapq.heappush(que, [0, 0, 0])  # dist, i, j
    dist[0][0] = 0

    while que:
        d, i, j = heapq.heappop(que)

        if i == N - 1 and j == N - 1:
            print('#{} {}'.format(k, d))
            break

        if d > dist[i][j]:  # visited 대체, heappop이 que에서 최소 가중치를 가지는 데이터를 꺼내오므로 그 이전에 들어갔던 데이터가 존재한다면 무시
            continue

        # 3. 현재 위치에서 갈 수 있는 위치들을 한번 보자
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < N and 0 <= nj < N:
                extra = 0 # 추가연료소모량
                if arr[ni][nj] > arr[i][j]: # 더 높은 지역일 경우
                    extra = arr[ni][nj] - arr[i][j]
                nd = d + extra + 1

                # 4. 만약에, 현재까지 쌓아온 가중치 + 현재에서 다음으로가는 가중치가 시작~다음위치까지 가는 가중치보다 작다면 업데이트
                # 처음에 저장되어 있는 시작~ 다음위치의 값들은 전부 무한대로 세팅했으므로 최초로 그 지점을 볼 때는 업데이트 된다.
                # 하지만 나중에 다른 노드를 거쳐서 다시 같은 지점을 가는 경우를 본다면, 지금 이상황이 이전에 왔던 것과 지금 가는것, 그 둘을 비교하는 상황이다
                if dist[ni][nj] > nd:
                    dist[ni][nj] = nd
                    heapq.heappush(que, [nd, ni, nj]) # 5. 후에 이 노드에서 연결된 다른곳이 있는지 확인하기 위해 최소힙에 넣는다.
