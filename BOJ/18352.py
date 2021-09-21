from collections import deque

N, M, K, X = map(int, input().split())

v = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
for i in range(M):
    s, e = map(int, input().split())
    v[s].append(e)

que = deque()
que.append(X)
visited[X] = True
depth = 0
ans = [-1]
while que:
    if depth == K:
        ans = sorted(list(que))
        break

    size = len(que)

    for _ in range(size):
        temp = que.popleft()
        for i in v[temp]:
            if visited[i]:
                continue
            que.append(i)
            visited[i] = True

    depth += 1

for i in ans:
    print(i)