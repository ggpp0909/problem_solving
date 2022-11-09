import sys
sys.stdin = open('input.txt')

temp = list(map(int, input().split()))
v = [[] for i in range(8)] # 노드 7개
visited = [False for i in range(8)]

for i in range(0, len(temp), 2):
    v[temp[i]].append(temp[i + 1])

def dfs(cur):
    print(cur, end=' ')
    for i in v[cur]:
        if visited[i]:
            continue
        visited[i] = True
        dfs(i)
        
dfs(1)
