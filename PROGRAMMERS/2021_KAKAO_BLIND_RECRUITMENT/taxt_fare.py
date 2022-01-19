import heapq

def dikstra(i, a, b, s, n, v):
    dist = [99999999 for i in range(n + 1)]
    que = []
    heapq.heappush(que, [0, i])
    dist[i] = 0

    while que:
        d, cur = heapq.heappop(que)

        if dist[cur] < d:
            continue

        for i in v[cur]:
            nd = d + i[1]
            if dist[i[0]] > nd:
                dist[i[0]] = nd
                heapq.heappush(que, [nd, i[0]])

    result = dist[s] + dist[a] + dist[b]
    # print(result)
    return result

# 헤어지는 지점을 x라고 하면
# s에서 x까지  + x에서 a까지 + x에서 b까지 더한 비용중 최소가 정답
# 임의의 노드 x에서 a, b, s로가는 비용을 다익스트라로 완탐하여 min값 업데이트
def solution(n, s, a, b, fares): # 노드수, 출발위치, a의도착, b의도착, 요금
    v = [[] for i in range(n + 1)]
    for i in fares:
        v[i[0]].append([i[1], i[2]])    # 양방향
        v[i[1]].append([i[0], i[2]])

    ans = 9999999
    for i in range(n + 1):
        ans = min(ans, dikstra(i, a, b, s, n, v))

    # print(ans)
    return ans