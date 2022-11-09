def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def union(x, y):
    x = find(x)
    y = find(y)

    par[x] = y


N, M = map(int, input().split())
school = [0] + input().split()
temp = [list(map(int, input().split())) for i in range(M)]
temp.sort(key=lambda x: x[2])
par = list(range(N + 1))

ans = 0
for i in temp:
    if find(i[0]) == find(i[1]) or school[i[0]] == school[i[1]]:
        continue
    ans += i[2]
    union(i[0], i[1])

for i in range(1, N + 1):
    find(i)


if len(set(par[1:])) == 1:
    print(ans)
else:
    print(-1)