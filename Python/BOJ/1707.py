from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)


K = int(sys.stdin.readline().rstrip())


# 색은 1, -1 로 표현
def is_BG(cur, color):
    global ans
    # if ans == "NO":
    #     return

    # if color_arr[cur] == color:
    #     ans = "NO"
    #     return

    color_arr[cur] = color
    for i in v[cur]:
        if color_arr[i]:
            if color_arr[i] == color:
                ans = "NO"
                return
            continue
        is_BG(i, -color)


def bfs(cur, color):
    global ans

    que = deque()
    que.append([cur, color])
    color_arr[cur] = color

    while que:
        now, color_ = que.popleft()
        color_arr[now] = color_

        for i in v[now]:
            if color_arr[i] == color_:
                ans = "NO"
                return
            que.append([i, -color_])


for _ in range(K):
    V, E = map(int, sys.stdin.readline().rstrip(). split())
    v = [[] for _ in range(V + 1)]

    for i in range(E):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        v[a].append(b)
        v[b].append(a)

    ans = "YES"
    color_arr = [0 for i in range(V + 1)]
    for i in range(1, V + 1):
        if color_arr[i]:
            continue
        if ans == "NO":
            break
        is_BG(i, 1)
        # bfs(i, 1)

    print(ans)
