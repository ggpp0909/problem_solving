N, M, t = map(int, input().split())

v = [[] for i in range(N)]
par = list(range(N + 1))

arr = [list(map(int, input().split())) for i in range(M)]

# 도시 N개면 n-2번의 정복비 증가
# N(N+1)// 2에 N-2 대입 -> (N-2)(N-1)//2 번의 정복비 증가
extra_fee = t * (((N - 2) * (N - 1)) // 2)

def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]

def union(x, y):
    x = find(x)
    y = find(y)
    par[x] = y

arr.sort(key=lambda x:x[2])
ans = 0
# print(arr)
for i in range(len(arr)):
    n1 = arr[i][0]
    n2 = arr[i][1]
    w = arr[i][2]
    if find(n1) == find(n2):
        continue
    union(n1, n2)
    ans += w

print(ans + extra_fee)

