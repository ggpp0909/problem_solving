import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    que = []
    heapq.heappush(que, [0, start])
    dist = [999999999 for i in range(n + 1)]
    dist[start] = 0
    while que:
        d, cur = heapq.heappop(que)

        for i in v[cur]:
            nd = d + i[1]

            if dist[i[0]] > nd:
                dist[i[0]] = nd
                heapq.heappush(que, [nd, i[0]])

    return dist

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    destination = []

    v = [[] for i in range(n + 1)]
    for i in range(m):
        a, b, d = map(int, input().split())

        v[a].append([b, d])
        v[b].append([a, d])

    for i in range(t):
        destination.append(int(input()))

    s_ = dijkstra(s)
    g_ = dijkstra(g)
    h_ = dijkstra(h)
    ans = []

    for i in destination:
        if s_[g] + g_[h] + h_[i] == s_[i] or s_[h] + h_[g] + g_[i] == s_[i]:
            ans.append(i)
    ans.sort()

    print(*ans)