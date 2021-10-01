import sys
sys.stdin = open('input.txt', encoding='UTF8')

def dfs(S, G):
    global ans
    visited[S] = True  # S 번 노드를 갔으면 다시는 들르지마
    for nxt in arr[S]:  # S 번 노드에서 갈수 있는 노드정보가 있는 리스트 순회
        if nxt == G:
            ans = 1
        if ans:     # 답 구했으면 더 할필요 없음
            return
        if visited[nxt]:  # 한번 들렀으면 가지마
            continue
        dfs(nxt, G)  # 안들렀으면 ㄱㄱ

n = int(input())

for k in range(1, n + 1):
    V, E = map(int, input().split())
    visited = [False for j in range(V + 1)]
    arr = [[] for i in range(V + 1)]
    ans = 0
    for i in range(E):
        s, e = map(int, input().split())
        arr[s].append(e)  # node를 arr의 인덱스로 맞춰서 해당 노드부터 갈수잇는 노드 저장

    S, G = map(int, input().split())
    dfs(S, G)
    print('#{} {}'.format(k, ans))


