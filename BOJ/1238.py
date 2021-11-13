import heapq
import sys

N, M, X = map(int, input().split())
temp = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(M)]
v = [[] for i in range(N + 1)]

for i in range(M):
    v[temp[i][0]].append([temp[i][1], temp[i][2]])

# X에서 각 마을로 갈수 있는 최단거리를 dist_1에 저장
dist_1 = [999999999999 for i in range(N + 1)]
que = []
heapq.heappush(que, [0, X])
dist_1[X] = 0

while que:
    d, cur = heapq.heappop(que)

    if d > dist_1[cur]:
        continue

    for i in v[cur]:
        nd = d + i[1]
        if nd < dist_1[i[0]]:
            dist_1[i[0]] = nd
            heapq.heappush(que, [nd, i[0]])


ans = 0
# 각 마을에서 X로 갈 수 있는 최단거리가 나올때마다 정답을 갱신
# 이전에 구했던 X->마을 이 저장된 dist_1의 값 + 지금 구하는 마을->X 의 최단거리
for i in range(1, N + 1):
    dist_2 = [9999999999 for i in range(N + 1)]
    que = []
    heapq.heappush(que, [0, i])
    dist_2[i] = 0

    if i == X:
        continue

    while que:
        d, cur = heapq.heappop(que)

        if d > dist_2[cur]:
            continue

        if cur == X:
            ans = max(ans, dist_1[i] + d)


        for j in v[cur]:
            nd = d + j[1]
            if nd < dist_2[j[0]]:
                dist_2[j[0]] = nd
                heapq.heappush(que, [nd, j[0]])

print(ans)