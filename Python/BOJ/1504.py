import heapq
import sys

N, E = map(int, sys.stdin.readline().rstrip().split())
temp = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(E)]
v = [[] for i in range(N + 1)]
for i in range(E):
    a, b, c = temp[i]
    v[a].append([b, c])
    v[b].append([a, c])


def dikstra(start, end):
    dist = [9999999999 for i in range(N + 1)]
    que = []
    heapq.heappush(que, [0, start])
    dist[start] = 0

    while que:
        d, cur = heapq.heappop(que)

        if cur == end:
            return d

        if dist[cur] < d:
            continue

        for i in v[cur]:
            nd = d + i[1]
            if dist[i[0]] > nd:
                dist[i[0]] = nd
                heapq.heappush(que, [nd, i[0]])
    # 경로 없으면
    else:
        return 9999999999

v1, v2 = map(int, input().split())
path1_1 = dikstra(1,v1)
path1_2 = dikstra(v1, v2)
path1_3 = dikstra(v2, N)

path2_1 = dikstra(1,v2)
path2_2 = dikstra(v2,v1)
path2_3 = dikstra(v1,N)

ans1 = ans2 = 0

ans1 = path1_1 + path1_2 + path1_3
ans2 = path2_1 + path2_2 + path2_3

if ans1 >= 9999999999 and ans2 >= 9999999999:
    print(-1)
else:
    print(min(ans1, ans2))
