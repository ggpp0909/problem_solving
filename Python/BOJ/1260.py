N, M, V = map(int, input().split())
temp = [list(map(int, input().split())) for i in range(M)]
v = [[] for i in range(N + 1)]

for i in temp:
    v[i[0]].append(i[1])
    v[i[1]].append(i[0])

for i in range(len(v)):
    v[i] = sorted(list(set(v[i])))


visited1 = [False for i in range(N + 1)]
visited2 = [False for i in range(N + 1)]
visited1[V] = True
visited2[V] = True
ans = [V]
def dfs(cur=V):
    for i in v[cur]:
        if visited1[i]:
            continue
        visited1[i] = True
        ans.append(i)
        dfs(i)
dfs()
print(*ans)

ans = [V]
def bfs(cur=V):
    while ans:
        temp = ans.pop(0)
        print(temp, end=' ')
        for i in v[temp]:
            if visited2[i]:
                continue
            visited2[i] = True
            ans.append(i)
bfs()
