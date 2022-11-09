import heapq
import sys

V, E = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(E)]

v = [[] for i in range(V + 1)]

for i in arr:
    v[i[0]].append([i[2], i[1]])  # 가중치 먼저

dist = [999999 for i in range(V + 10)]
dist[K] = 0
que = []
heapq.heappush(que, [0, K])

while que:
    d, cur = heapq.heappop(que)

    if dist[cur] < d:
        continue

    for i in v[cur]:
        nd = d + i[0]
        if dist[i[1]] > nd:
            dist[i[1]] = nd
            heapq.heappush(que, [nd, i[1]])


for i in range(1, V + 1):
    if dist[i] == 999999:
        print("INF")
    else:
        print(dist[i])
