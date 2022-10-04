import sys
sys.setrecursionlimit(100000)

par = [i for i in range(5010)]
sz = [1 for i in range(5010)]

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    par[a] = b
    sz[b] += sz[a]

n, q = map(int, input().split())
v = [list(map(int, input().split())) for i in range(n - 1)]
query = [list(map(int, input().split())) + [i] for i in range(q)]
ans = [0 for i in range(5010)]

v.sort(key=lambda x:x[2]) # v는 k기준 오름차순
query.sort() 

idx = len(v) - 1
for i in query[::-1]: # 내림차순
    while idx >= 0 and v[idx][2] >= i[0]:
        union_(v[idx][0], v[idx][1])
        idx -= 1

    ans[i[2]] = sz[find(i[1])] - 1

for i in range(q):
    print(ans[i])