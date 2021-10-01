import sys
sys.stdin = open('input.txt', encoding='UTF8')

temp = list(map(int,input().split()))
arr=[[] for i in range(10)]
visited = [False for i in range(10)]  # 들른곳은 다시 안들른다? -> 방문 처리

for i in range(0,len(temp),2):
    arr[temp[i]].append(temp[i+1])  # node를 arr의 인덱스로 맞춰서 해당 노드부터 갈수잇는 노드 저장
    arr[temp[i+1]].append(temp[i])

for i in arr:   # 각 노드에서 갈 수 있는 노드를 정렬하여 작은 노드 우선으로 탐색하도록 함
    i.sort()

ans = []
def dfs(cur):
    ans.append(str(cur))  # 나중에 join으로 '-' 넣으려고 리스트에 str로 저장

    visited[cur] = True     # cur 번 노드를 갔으면 다시는 들르지마
    for nxt in arr[cur]:    # cur번 노드에서 갈수 있는 노드정보가 있는 리스트 순회
        if visited[nxt]:    # 한번 들렀으면 가지마
            continue
        dfs(nxt)            # 안들렀으면 ㄱㄱ

dfs(1)
print('-'.join(ans))
