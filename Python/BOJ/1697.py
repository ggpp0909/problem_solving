from collections import deque

n, m = map(int, input().split())
visited = [False for i in range(100001)]

que = deque()
que.append([n, 0])
visited[n] = True

while que:
    temp = que.popleft()
    depth = temp[1]

    if temp[0] == m:
        print(depth)
        break

    a = temp[0] - 1
    b = temp[0] + 1
    c = temp[0] * 2

    if 0 <= a <= 100000 and not visited[a]:
        que.append([a, depth + 1])
        visited[a] = True

    if 0 <= b <= 100000 and not visited[b]:
        que.append([b, depth + 1])
        visited[b] = True

    if 0 <= c <= 100000 and not visited[c]:
        que.append([c, depth + 1])
        visited[c] = True