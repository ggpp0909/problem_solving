import sys
sys.stdin = open('input.txt')

# MST -> 크루스칼알고리즘 -> UF

def find(x): # x의 루트를 찾는 함수
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]   # path compression

def union_(x, y):
    x = find(x)
    y = find(y)

    # union by rank
    if rank[x] > rank[y]:
        par[y] = x
    elif rank[x] < rank[y]:
        par[x] = y
    else:
        par[x] = y
        rank[y] += 1

T = int(input())

for k in range(1, T + 1):
    V, E = map(int, input().split())
    par = list(range(V + 1))
    rank = [0 for i in range(V + 1)]

    arr = []
    for i in range(E):
        n1, n2, w = map(int, input().split())
        arr.append([n1, n2, w])

    arr.sort(key= lambda x: x[2])   # 가중치 순으로 오른차순 정렬
    # (크루스칼알고리즘: 각 노드에서 다른 노드로 향하는 가중치중 최소값만을 찾아서 연결하면 MST가 된다는 것을 이용)

    ans = 0
    for i in range(len(arr)):
        n1 = arr[i][0]
        n2 = arr[i][1]
        w = arr[i][2]
        if find(n1) == find(n2): # 이미 연결되 있으면 넘어가
            continue
        ans += w    # 아니라면 가중치 +, 연결시켜
        union_(n1, n2)

    print('#{} {}'.format(k, ans))

