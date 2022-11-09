def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def union(x, y):
    x = find(x)
    y = find(y)

    par[x] = y


N = int(input())
temp = [list(map(int, input().split())) for i in range(N)]
par = list(range(N + 1))

# temp 가공
edge = []
for i in range(N):
    for j in range(N):
        edge.append([i, j, temp[i][j]])

edge.sort(key=lambda x: x[2])

ans = 0
for i in range(len(edge)):
    if find(edge[i][0]) == find(edge[i][1]):
        continue
    ans += edge[i][2]
    union(edge[i][0], edge[i][1])

print(ans)