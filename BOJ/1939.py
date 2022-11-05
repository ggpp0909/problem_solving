import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
N, M = map(int, input().split())
v = []
for _ in range(M):
    v.append(list(map(int, input().split())))

S, E = map(int, input().split())

# 아니면 최대 신장트리 만들고 dfs나 bfs?

par = list(range(N + 1))

def find(x):
    if par[x] == x:
        return x

    par[x] = find(par[x])
    return par[x]

def union(x, y):
    x = find(x)
    y = find(y)

    par[x] = y


v.sort(key=lambda x:x[2], reverse=True)
v2 = [[] for i in range(N + 1)] # 인접리스트
# print(v)

# 최대신장 트리 만들면서 간선정보 만들기
for i in v:
    x = find(i[0])
    y = find(i[1])
    if x == y:
        continue
    v2[i[0]].append([i[1], i[2]])
    v2[i[1]].append([i[0], i[2]])
    union(x, y)

def dfs(cur, ans):
    if cur == E:
        print(ans)
        return

    for i in v2[cur]:
        if visited[i[0]]:
            continue
        visited[i[0]] = True
        dfs(i[0], min(ans, i[1]))

# print(v2)
for i in v2[S]:
    visited = [False for i in range(N + 1)]
    visited[S] = True
    dfs(i[0], i[1])

