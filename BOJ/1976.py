N = int(input())
M = int(input())

arr = [list(map(int, input().split())) for i in range(N)]
plan = list(map(int, input().split()))
par = list(range(N + 1))
# print(arr)
def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def union(x, y):
    x = find(x)
    y = find(y)
    par[x] = y

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            if find(i + 1) != find(j + 1):
                union(i + 1, j + 1)
        else:
            continue
temp = find(plan[0])
ans = "YES"
for i in plan:
    if find(i) != temp:
        ans = "NO"
        break
print(ans)



