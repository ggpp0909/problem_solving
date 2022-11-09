import sys
sys.stdin = open('input.txt')

def dfs(cur, cnt):
    global ans
    ans = max(ans, cnt)

    for i in v[cur]:
        if visited[i]:
            continue
        visited[i] = True
        dfs(i, cnt + 1)
        visited[i] = False

T = int(input())

for k in range(1, T + 1):
    N, M = map(int, input().split())    # 정점 간선
    visited = [False for i in range(N + 1)]
    v = [[] for i in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        v[x].append(y)
        v[y].append(x)


    ans = 1
    for i in range(1, N + 1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False

    print('#{} {}'.format(k, ans))




