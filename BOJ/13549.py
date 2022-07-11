from collections import deque

N, K = map(int, input().split())
visited = [False for i in range(100001)]

que = deque()
que.append([N, 0])  # [위치, 걸린시간]
visited[N] = True
ans = 999999

while que:
    location, time = que.popleft()

    if location == K:
        ans = min(ans, time)

    temp1 = location * 2
    temp2 = location + 1
    temp3 = location - 1

    for i in [[temp1, time], [temp2, time + 1], [temp3, time + 1]]:
        if 0 <= i[0] <= 100000 and not visited[i[0]]:
            visited[i[0]] = True
            que.append([i[0], i[1]])

print(ans)
