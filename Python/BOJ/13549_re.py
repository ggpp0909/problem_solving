from collections import deque

N, K = map(int, input().split())
visited = [999999 for i in range(100001)] # 계속 업데이트 해야 함(순간이동은 0초가 걸리기 때문)ㄴ

que = deque()
que.append([N, 0])  # [위치, 걸린시간]
visited[N] = True
ans = 999999

while que:
    location, time = que.popleft()

    if location == K:
        ans = min(ans, time)

    nloation1 = location * 2
    nloation2 = location + 1
    nloation3 = location - 1

    for i in [[nloation1, time], [nloation2, time + 1], [nloation3, time + 1]]:
        if 0 <= i[0] <= 100000 and visited[i[0]] > i[1]:  # 조건, 가지치기
            visited[i[0]] = i[1]
            que.append([i[0], i[1]])

print(ans)
