n, m = map(int, input().split())
par = [i for i in range(n + 1)]

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union_(x, y):
    x = find(x)
    y = find(y)
    par[x] = y

for _ in range(m):
    a, b = map(int, input().split())
    union_(a, b)

arr = []
for i in range(1, n + 1):
    arr.append(find(i))

arr = list(set(arr))

print(len(arr))