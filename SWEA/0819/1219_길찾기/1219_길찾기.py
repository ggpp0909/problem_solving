import sys
sys.stdin = open('input.txt', encoding='UTF8')

def dfs(cur=0):
    global ans
    visited[cur] = True

    for nxt in arr[cur]:
        if visited[nxt]:
            continue
        if nxt == 99:
            ans = 1
        if ans:
            return
        dfs(nxt)

for k in range(1, 11):
    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    arr = [[] for i in range(m + 1)]
    visited = [False for i in range(101)]
    ans = 0
    for i in range(0, len(temp), 2):
        arr[temp[i]].append(temp[i + 1])  # node를 arr의 인덱스로 맞춰서 해당 노드부터 갈수잇는 노드 저장

    dfs()
    print('#{} {}'.format(k, ans))