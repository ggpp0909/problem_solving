# 강철 부대로부터 bfs -> 실패
# 완탐 + 다익
from collections import deque
import heapq

def solution(n, roads, sources, destination):
#     visited = [False for i in range(n + 1)]
#     v = [[] for i in range(n + 1)]
#     for i in roads:
#         v[i[1]].append(i[0])
        
#     que = deque()
#     que.append([destination, 0])
#     dist = [-1 for i in range(n + 1)]
#     dist[destination] = 0
    
#     while que:
#         cur, depth = que.popleft()
        
#         for i in v[cur]:
#             dist[i] = depth
#             que.append([i, depth + 1])
            
#     print(dist)
    v = [[] for i in range(n + 1)]
    for i in roads:
        v[i[0]].append(i[1])
        v[i[1]].append(i[0])
    
    ans = []
    que = []
    dist = [9999999 for i in range(n + 1)]
    heapq.heappush(que, [0, destination])
    dist[destination] = 0

    while que:
        d, cur = heapq.heappop(que)

        if d > dist[cur]:
            continue

        for j in v[cur]:
            nd = d + 1
            if nd <= dist[j]:
                dist[j] = nd
                heapq.heappush(que, [nd, j])
                
    for i in sources:
        if dist[i] == 9999999:
            ans.append(-1)
        else:
            ans.append(dist[i])
    return ans