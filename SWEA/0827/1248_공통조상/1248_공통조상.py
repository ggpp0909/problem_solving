import sys
sys.stdin = open('input.txt')
n = int(input())

def dfs(cur=1):  # 루트는 1
    for nxt in edge[cur]:
        par[nxt] = cur # nxt로 들어가기전에, cur은 nxt의 부모다 저장
        dfs(nxt)
        sz[cur] += sz[nxt] # 각 노드의 서브트리 크기는 왼, 오 서브트리 크기 합

def tracking_par(N): # N의 조상을 리스트로 반환하는 함수
    temp_arr = []
    temp = N
    while temp:
        temp_arr.append(par[temp])
        temp = par[temp]
    return temp_arr

for k in range(1, n + 1):
    V, E, node_1, node_2 = map(int, input().split())
    par = [0 for i in range(V + 1)]     # 인덱스: 자식, 값: 부모
    sz = [1 for i in range(V + 1)]      # 각 노드(인덱스)의 서브트리크기
    temp = list(map(int, input().split()))
    edge = [[] for i in range(V + 1)]   # 인접리스트
    for i in range(0, len(temp), 2):
        edge[temp[i]].append(temp[i + 1])

    dfs()

    node1_arr = tracking_par(node_1)
    node2_arr = tracking_par(node_2)
    dif = min(len(node1_arr), len(node2_arr))
    for i in range(-dif, -1): # 공통노드찾기
        if node1_arr[i] == node2_arr[i]:
            common = node1_arr[i]()
            break

    print('#{} {} {}'.format(k, common, sz[common]))
