from collections import deque

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

t = int(input())
for _ in range(t):
    n = int(input())
    home_i, home_j = map(int, input().split())
    cv = []
    for i in range(n):
        cv.append(list(map(int, input().split())))
    dest_i, dest_j = map(int, input().split())
    visited = {}

    # 맥주 20병으로 갈 수 있는거리 1000, 즉 다음 지점까지 1000 미만이면 못감.
    que = deque()
    que.append([home_i, home_j])
    visited[(home_i, home_j)] = False

    ans = 'sad'
    while que:
        i, j = que[0][0], que[0][1]
        que.popleft()

        # 현재 위치에서 목적지까지 1000만에 갈 수 있다?
        if distance(i, j, dest_i, dest_j) <= 1000:
            ans = 'happy'
            break

        # 현재 위치에서 편의점까지 1000만에 갈 수 있다? que에 넣어
        for k in range(len(cv)):
            cv_i = cv[k][0]
            cv_j = cv[k][1]
            if distance(i, j, cv_i, cv_j) <= 1000 and visited.get((cv_i, cv_j), True):
                visited[(cv_i, cv_j)] = False
                que.append([cv_i, cv_j])

    print(ans)