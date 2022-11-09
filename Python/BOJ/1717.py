import sys
sys.setrecursionlimit(10 ** 6)

def find(x):
    if x == par[x]:
        return par[x]
    else:
        par[x] = find(par[x])
        return par[x]

def union(x, y):
    x = find(x)
    y = find(y)
    par[x] = y

n, m = map(int, sys.stdin.readline().rstrip().split())

par = [i for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 0:
        union(b, c)
    if a == 1:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')

