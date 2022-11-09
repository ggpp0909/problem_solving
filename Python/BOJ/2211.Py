import sys, heapq
input = sys.stdin.readline

# 한 노드에서 다른 모든노드로 가는 최단거리 -> 다익스트라
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(M)]
dist = [999999999 for i in range(N + 1)]

# 인접리스트
v = [[] for i in range(N + 1)]
for i in arr:
    v[i[0]].append([i[1], i[2]])
    v[i[1]].append([i[0], i[2]])



que = []
# 1번노드에서 시작
heapq.heappush(que, [0, 1, -1]) # 가중치, 현재노드번호, 이전 노드번호
dist[1] = 0
ans = []
while que:
    d, cur, pre = heapq.heappop(que) 

    if dist[cur] < d:
        continue

    ans.append([cur, pre])
    
    for i in v[cur]:
        nd = d + i[1]
        if nd < dist[i[0]]:
            dist[i[0]] = nd
            heapq.heappush(que, [nd, i[0], cur])

print(len(ans) - 1)
for i in range(1, len(ans)):
    print(*ans[i])