import sys
import heapq
sys.stdin = open('input.txt')

# 가중치가 존재할때 최단경로를 찾는 알고리즘 - 다익스트라
# 알고리즘에서는 heapq(최소힙)를 import해서 사용하여 간단하게 구현 가능
# 코드구조는 BFS와 유사

T = int(input())

for k in range(1, T + 1):
    N, E = map(int, input().split())
    temp = [list(map(int, input().split())) for i in range(E)]    # [[s, e, w], ...]
    dist = [9999 for i in range(N + 1)] # 초기 모든 노드 가중치 무한대로 세팅
    v = [[] for i in range(N + 1)]
    for i in temp:
        v[i[0]].append([i[1], i[2]])  # 연결리스트는 단방향, 가중치를 함께저장

    # 시작노드 가중치 0으로 세팅하고 출발
    que = []
    heapq.heappush(que, [0, 0])  # 가중치, idx
    dist[0] = 0

    while que:
        d, cur = heapq.heappop(que)  # 가중치중 가장 작은애를 뽑아, 시작~ 현재위치까지 쌓아온 가중치, cur이 현재위치

        if cur == N:
            print('#{} {}'.format(k, d))
            break

        if d > dist[cur]:   # visited 대체
            continue

        # 현재 위치에서 갈 수 있는 위치들을 한번 보자
        # 만약에, 현재까지 쌓아온 가중치 + 현재에서 다음으로가는 가중치가 시작~다음위치까지 가는 가중치보다 작다면 업데이트
        for i in v[cur]:
            nd = dist[cur] + i[1]
            if dist[i[0]] > nd:
                dist[i[0]] = nd
                heapq.heappush(que, [nd, i[0]])
