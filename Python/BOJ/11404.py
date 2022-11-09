# 다익스트라

# import heapq
# import sys
#
# n = int(sys.stdin.readline().rstrip())
# m = int(sys.stdin.readline().rstrip())
# v = [[] for i in range(n + 1)]
# INF = int(1e9)
#
# for i in range(m):
#     a, b, c = map(int, sys.stdin.readline().rstrip().split())
#     v[a].append([b, c])
#
# def dijkstra(i):
#     dist = [INF for k in range(n + 1)]
#     que = []
#     dist[i] = 0
#     heapq.heappush(que, [0, i])
#     while que:
#         d, s = heapq.heappop(que)
#
#         if d > dist[s]:
#             continue
#
#         for k in v[s]:
#             nd = d + k[1]
#
#             if dist[k[0]] > nd:
#                 dist[k[0]] = nd
#                 heapq.heappush(que, [nd, k[0]])
#
#     for k in range(1, n + 1):
#         if dist[k] == INF:
#             print(0, end=' ')
#         else:
#             print(dist[k], end=' ')
#
# for i in range(1, n + 1):
#     dijkstra(i)
#     print()
#

# 플로이드 와샬
n = int(input())
m = int(input())
INF = int(1e9)
dp = [[INF for i in range(n)] for j in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    dp[a - 1][b - 1] = min(dp[a - 1][b - 1], c)

for k in range(n): # 경유지
    for i in range(n): # 출발지
        for j in range(n): # 도착지
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = 0
        else:
            if dp[i][j] == INF:
                dp[i][j] = 0

for i in dp:
    print(*i)