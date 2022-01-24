from collections import deque

def solution(places):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    ans = []
    for place in places:
        flag = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    visited = [[False for i in range(5)] for j in range(5)]
                    que = deque()
                    que.append([i, j, 0])
                    visited[i][j] = True
                    while que:
                        x, y, depth = que.popleft()
                        if depth == 3 or flag == 0:
                            break

                        for dir in range(4):
                            nx = x + di[dir]
                            ny = y + dj[dir]
                            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and place[nx][ny] != 'X':
                                if place[nx][ny] == 'O':
                                    visited[nx][ny] = True
                                elif place[nx][ny] == 'P':
                                    if depth + 1 <= 2:
                                        flag = 0
                                        # print(len(ans), nx, ny)
                                        break
                                que.append([nx, ny, depth + 1])

        ans.append(flag)
    return ans

# solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])