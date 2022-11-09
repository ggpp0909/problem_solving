from collections import deque

a, b = map(int, input().split())
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(M)]

v = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]

for i in range(M):
    v[arr[i][0]].append(arr[i][1])
    v[arr[i][1]].append(arr[i][0])


que = deque()
que.append([a, 0])
visited[a] = True
def bfs():
    global ans
    cnt = 0

    while que:
        cur, cnt = que.popleft()

        # print(cur)
        if cur == b:
            return cnt

        for i in v[cur]:
            if visited[i]:
                continue
            visited[i] = True
            que.append([i, cnt + 1])

    else:
        return -1

print(bfs())
