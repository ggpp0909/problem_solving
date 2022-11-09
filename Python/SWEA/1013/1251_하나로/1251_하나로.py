import sys
sys.stdin = open('input.txt')

def find(x):
    if par[x] == x:
        return x
    else:
        #path compression
        par[x] = find(par[x])
        return par[x]

def union_(x, y):  # x와 y가 속한 집합을 합쳐주는함수(한쪽의 루트를 다른 루트밑에 붙인다)
    x = find(x)
    y = find(y)

    # union by rank
    if rank[x] < rank[y]:
        par[x] = y
    elif rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y
        rank[y] += 1   # rank가 같을때, 루트로 삼은 부분의 rank 증가

T = int(input())

for k in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    par = list(range(N + 1))  # 해당 요소의 부모 요소값
    rank = [0 for i in range(N + 1)]  # 해당 인덱스값이 루트인 트리의 최대 depth

    arr = []
    for i in range(N):
        for j in range(N):
            dis = ((X[i] - X[j]) ** 2) + ((Y[i] - Y[j]) ** 2)
            arr.append((dis, i, j)) # 거리, 섬1, 섬2 정보 싹다 구해서 정렬
    arr.sort(key=lambda x: x[0])

    ans = 0
    for i in range(len(arr)):
        if find(arr[i][1]) == find(arr[i][2]):
            continue
        ans += arr[i][0] * E
        union_(arr[i][1], arr[i][2])

    print('#{} {}'.format(k, round(ans)))






