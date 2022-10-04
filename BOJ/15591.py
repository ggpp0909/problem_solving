import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, Q = map(int, input().split())
v = [[] for i in range(N + 1)]

for i in range(N - 1):
    a, b, c = map(int, input().split())
    v[a].append([b, c])
    v[b].append([a, c])

# 유사도는 노드를 하나씩 멀리 갈수록 줄어들면 줄어들지 늘어나지 않음
# bfs나 dfs로 유사도가 k보다 큰 애들까지만 개수 cnt

def dfs(cur):
    global cnt, K
    for i in v[cur]:
        if not visited[i[0]] and i[1] >= K:
            visited[i[0]] = True
            cnt += 1
            dfs(i[0])

def bfs(start):
    global cnt
    
    que = deque()
    que.append(start)
    while que:
        cur = que.popleft()
        for i in v[cur]:
            if not visited[i[0]] and i[1] >= K:
                visited[i[0]] = True
                cnt += 1
                que.append(i[0])

for _ in range(Q):
    K, V = map(int, input().split())
    cnt = 0
    visited = [False for i in range(N + 1)]
    visited[V] = True
    bfs(V)
    print(cnt)