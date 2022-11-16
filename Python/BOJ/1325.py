import sys
from collections import deque
input = sys.stdin.readline
# # union find 연결하면서 사이즈배열 업데이트, 사이즈배열 제일 큰놈만 프린트
# # -> 부모를 자꾸 갈아끼워서 실패..
# def find(x):
#     if x == par[x]:
#         return x

#     par[x] = find(par[x])
#     return par[x]

# def union(x, y):
#     x = find(x)
#     y = find(y)

#     par[x] = y
#     sz[y] += sz[x]

# N, M = map(int, input().split())
# par = list(range(N + 1))
# sz = [1 for i in range(N + 1)]

# for i in range(M):
#     x, y = map(int, input().split())
#     union(x, y)

# print(sz)

# 아이디어 2 dfs
N, M = map(int, input().split())
v = [[] for i in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    v[y].append(x) # 거꾸로 연결

node_sum = [1 for i in range(N + 1)]

def dfs(cur):
    # 이미 구했으면 리턴
    if node_sum[cur] != 1:
        return node_sum[cur]

    # 밑에달린애들 탐색하면서 더하면서 나오기
    for i in v[cur]:
        node_sum[cur] += dfs(i)

    return node_sum[cur]

def bfs(cur):
    if node_sum[cur] != 1:
        return
    que = deque()
    que.append(cur)
    visited = [False for i in range(N + 1)]
    visited[cur] = True
    while que:
        x = que.popleft()
        for i in v[x]:
            if visited[i]:
                continue
            visited[i] = True
            node_sum[cur] += 1
            que.append(i)
    

for i in range(1, N + 1):
    # dfs(i)
    bfs(i)
# print(node_sum)

max_value = max(node_sum)
for i in range(1, N + 1):
    if node_sum[i] == max_value:
        print(i, end=" ")

