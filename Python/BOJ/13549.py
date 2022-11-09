# from collections import deque

# N, K = map(int, input().split())
# visited = [999999 for i in range(100001)]

# que = deque()
# que.append([N, 0])  # [위치, 걸린시간]
# visited[N] = True
# ans = 100000

# while que:
#     location, time = que.popleft()

#     if location == K:
#         ans = min(ans, time)

#     temp1 = location * 2
#     temp2 = location + 1
#     temp3 = location - 1

#     for i in [[temp1, time], [temp2, time + 1], [temp3, time + 1]]:
#         if 0 <= i[0] <= 100000 and i[1] <= visited[i[0]]:  # 조건, 가지치기
#             visited[i[0]] = min(visited[i[0]], i[1])
#             que.append([i[0], i[1]])

# print(ans)

from collections import deque

N, K = map(int, input().split())
visited = [999999 for i in range(100001)]

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
        if 0 <= i[0] <= 100000 and visited[i[0]] > i[1]:  # 조건, 가지치기
            visited[i[0]] = i[1]
            que.append([i[0], i[1]])

print(ans)
