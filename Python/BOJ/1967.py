import sys
sys.setrecursionlimit(10**6)

n = int(input())
temp = [list(map(int, input().split())) for i in range(n - 1)]

v = [[] for i in range(n + 1)]
for i in temp:
    v[i[0]].append([i[1], i[2]])
    v[i[1]].append([i[0], i[2]])

ans = 0
n1 = 0
def dfs(cur, tot):
    global ans, n1
    for i in v[cur]:
        if visited[i[0]]:
            continue
        if ans <= tot + i[1]:
            ans = tot + i[1]
            n1 = i[0]

        visited[i[0]] = True
        dfs(i[0], tot + i[1])

visited = [False for i in range(n + 1)]
visited[1] = True
dfs(1, 0)

visited = [False for i in range(n + 1)]
visited[n1] = True
dfs(n1, 0)

print(ans)