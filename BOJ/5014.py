from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [False for i in range(F + 1)]

que = deque()
que.append([S, 0])
visited[S] = True

while que:
    cur, cnt = que.popleft()

    if cur == G:
        print(cnt)
        break

    if 1 <= cur + U <= F and not visited[cur + U]:
        visited[cur + U] = True
        que.append([cur + U, cnt + 1])

    if 1 <= cur - D <= F and not visited[cur - D]:
        visited[cur - D] = True
        que.append([cur - D, cnt + 1])

else:
    print("use the stairs")