import heapq
import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
v = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    v[a].append([b, c])

def dijkstra(i):
    dist = [999999 for k in range(n + 1)]
    que = []
    dist[i] = 0
    heapq.heappush(que, [0, i])
    while que:
        d, s = heapq.heappop(que)

        if d > dist[s]:
            continue

        for k in v[s]:
            nd = d + k[1]

            if dist[k[0]] > nd:
                dist[k[0]] = nd
                heapq.heappush(que, [nd, k[0]])

    for k in range(1, n + 1):
        if dist[k] == 999999:
            print(0, end=' ')
        else:
            print(dist[k], end=' ')

for i in range(1, n + 1):
    dijkstra(i)
    print()


