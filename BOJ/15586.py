import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    par[x] = y
    sz[y] += sz[x]

n, q = map(int, input().split()) # 노드 수, 쿼리 수
v = [list(map(int, input().split())) for i in range(n - 1)] # 연결 정보
query = [list(map(int, input().split())) + [i] for i in range(q)] # 쿼리 정보들, 쿼리 고유 인덱스 부여
ans = [0 for i in range(q)]

v.sort(key=lambda x:x[2], reverse=True) # v는 k기준 내림차순
query.sort(reverse=True) # 쿼리는 k기준 내림차순
# print(v)
# print(query)

par = list(range(n + 1))
sz = [1 for i in range(n + 1)]


idx = 0
for i in query: 
    while idx < len(v) and v[idx][2] >= i[0]:
        union(v[idx][0], v[idx][1])
        idx += 1

    ans[i[2]] = sz[find(i[1])] - 1 # 쿼리 인덱스에 답저장

for i in range(q):
    print(ans[i])