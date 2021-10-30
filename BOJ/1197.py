def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def union(x, y):
    x = find(x)
    y = find(y)
    par[x] = y


V, E = map(int, input().split())
par = list(range(V + 1))

arr = [list(map(int, input().split())) for i in range(E)]
arr.sort(key=lambda x: x[2])

ans = 0
for i in arr:
    if find(i[0]) == find(i[1]):
        continue
    ans += i[2]
    union(i[0], i[1])

print(ans)
