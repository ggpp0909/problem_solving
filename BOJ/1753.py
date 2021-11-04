import heapq, sys

V, E = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())

v = [[] for i in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().rstrip().split())
    v[s].append([e, w])

dist =[999999 for i in range(V + 1)]

que = []
dist[K] = 0
heapq.heappush(que, [0, K])

ans = []
while que:
    d, cur = heapq.heappop(que)

    if dist[cur] < d:
        continue

    ans.append([d, cur])

    for i in v[cur]:
        nxt = i[0]
        nd = d + i[1]
        if dist[nxt] > nd:
            dist[nxt] = nd
            heapq.heappush(que, [nd, nxt])

ans.sort(key=lambda x: x[1])

temp = ['INF' for i in range(V)]

for i in range(len(ans)):
    temp[ans[i][1]-1] = ans[i][0]

for i in range(V):
    print(temp[i])