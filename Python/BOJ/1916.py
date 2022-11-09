import heapq

N = int(input())
M = int(input())
temp = [list(map(int, input().split())) for i in range(M)]
s, e = map(int, input().split())
dist = [9999999999 for i in range(N + 1)]
v = [[] for i in range(N + 1)]

for i in temp:
    v[i[0]].append([i[1], i[2]])

que = []
heapq.heappush(que, [0, s])
dist[s] = 0

while que:
    d, cur = heapq.heappop(que)

    if cur == e:
        print(d)
        break

    if d > dist[cur]:
        continue

    for i in v[cur]:
        nd = d + i[1]
        if dist[i[0]] > nd:
            dist[i[0]] = nd
            heapq.heappush(que, [nd, i[0]])